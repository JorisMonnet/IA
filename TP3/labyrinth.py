import matplotlib.pyplot as plt
import numpy as np
from deap import base
from deap import creator
from deap import tools
from deap import algorithms
from collections import namedtuple
from functools import reduce
from enum import Enum
import operator,random,time,math   

def generate_field(M, N, P=.9):
    """ generate random grid """
    field = np.random.choice([0, 1], size=(M,N), p=[P, 1-P])
    field[0,0] = 0
    field[M-1,N-1] = 0
    return field
    
def display_labyrinth(grid, start_cell, end_cell, solution=None):
    """Display the labyrinth matrix and possibly the solution with matplotlib.
    Free cell will be in light gray.
    Wall cells will be in dark gray.
    Start and end cells will be in dark blue.
    Path cells (start, end excluded) will be in light blue.
    :param grid np.array: labyrinth matrix
    :param start_cell: tuple of i, j indices for the start cell
    :param end_cell: tuple of i, j indices for the end cell
    :param solution: list of successive tuple i, j indices who forms the path
    """
    grid = np.array(grid, copy=True)
    FREE_CELL = 19
    WALL_CELL = 16
    START = 0
    END = 0
    PATH = 2
    grid[grid == 0] = FREE_CELL
    grid[grid == 1] = WALL_CELL
    grid[start_cell] = START
    grid[end_cell] = END
    if solution:
        solution = solution[1:-1]
        for cell in solution:
            grid[cell] = PATH
    else:
        print("No solution has been found")
    plt.matshow(grid, cmap="tab20c")

def solve_labyrinth(grid, start_cell, end_cell, max_time_s):
    """Attempt to solve the labyrinth by returning the best path found
    :param grid np.array: numpy 2d array
    :start_cell tuple: tuple of i, j indices for the start cell
    :end_cell tuple: tuple of i, j indices for the end cell
    :max_time_s float: maximum time for running the algorithm
    :return list: list of successive tuple i, j indices who forms the path
    """
    def manhattanDistance(pointA, pointB):
        """Mahnattan distance between two points"""
        return abs(pointA[0]-pointB[0]) + abs(pointA[1]-pointB[1])

    def getChromosomePath(individual):
        """ Return the chromosome path from start to end or to the last cell if end is not found"""
        path = [start_cell]
        for Move in [MOVES[gene] for gene in individual]:
            path.append(Move.apply(path[-1])) #append each move to the current Position
            if path[-1] == end_cell : return path #current Position = end cell
        return path

    def fitness(individual, target):
        """ Fitness function of the chromosome :"""
        currentPos = start_cell #currentPos = the position we treat
        for i in range(len(individual)):
            gene = individual[i]
            nextPos = MOVES[gene].apply(currentPos) #nextPos = the next position after the move from the currentPos
            while nextPos[0] not in range(N) or  nextPos[1] not in range(N) or grid[nextPos[0]][nextPos[1]] != 0: #verify if a cell is not in the grid or is a wall
                individual[i] = random.randint(0, MAX_ENCODING) #create a random move
                nextPos = MOVES[individual[i]].apply(currentPos)
            currentPos = nextPos
            if currentPos == target: return (0, i+1) #return the number of iterations(+1 because currentPos = newPos just before so one iteration is missing)

        if start_cell == currentPos: return (50000,5000) #Not good beacause start cell = 0,0 so in the next line it will do manhattanDistance(target, currentPos)/0 !!
        return ((float(manhattanDistance(target, currentPos)) / manhattanDistance(start_cell, currentPos)), i+1)


    def evaluatePopulation(population, target):
        """Evaluate population function"""
        for ind in population:
            ind.fitness.values = toolbox.fitness(ind, target)

    #grid size = NxN
    N = grid.shape[0]

    CHROMOSOME_LENGTH = math.ceil(2*N / 10) #ceil = min 1       -> 10 to begin slowly 

    Move = namedtuple("Move", ["apply", "str"])
    MOVES = {
        0: Move(lambda position: (position[0]-1, position[1]), "left"),
        1: Move(lambda position: (position[0]+1, position[1]), "right"),
        2: Move(lambda position: (position[0], position[1]-1), "top"),
        3: Move(lambda position: (position[0], position[1]+1), "bottom")
    }
    MAX_ENCODING=len(MOVES)-1   #allow to just change MOVES by removing some magic number in fitness function

    #DEAP functions
    #creator 
    creator.create("FitnessMin", base.Fitness, weights=(-10000.0, -10.0))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    #toolBox from Base 
    toolbox = base.Toolbox()
    toolbox.register("fitness", fitness)
    toolbox.register("mate", tools.cxMessyOnePoint)
    toolbox.register("mutate", tools.mutUniformInt, low=0, up=MAX_ENCODING, indpb=0.1)
    toolbox.register("select", tools.selTournament)
    toolbox.register("init_gene", random.randint, 0, MAX_ENCODING)
    toolbox.register("init_individual", tools.initRepeat, creator.Individual, toolbox.init_gene, CHROMOSOME_LENGTH)
    toolbox.register("init_population", tools.initRepeat, list, toolbox.init_individual)
    toolbox.register("evaluate", evaluatePopulation)
    populationSize = 100
    population = toolbox.init_population(n=populationSize)
    toolbox.evaluate(population, end_cell)

    #Choosen parameters
    MUTPB = 0.65
    CXPB = 0.75
    tournoisSize = 10
    endTime = iterations = 0
    isPathFound = False
    count = 0 
    lastPath = 0

    startTime = time.time() #begin to work

    while endTime < max_time_s and count < 5: # magic number : stop when we found 5 times the same best path
        #tournament
        children = toolbox.select(population, len(population), tournoisSize)
        children = list(map(toolbox.clone, children))

        #crossover
        for child1, child2 in zip(children[::2], children[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
        #mutation
        for mutant in children:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)

        #evaluate children
        population = children
        toolbox.evaluate(population, end_cell)
        
        if not isPathFound:
            path = [ind.fitness.values for ind in population if ind.fitness.values[0] == 0]
            if path:
                isPathFound = True
                toolbox.register("mate", tools.cxOnePoint) #Path found, mutate with cxOnePoint
        else:
            #check if there is a better path
            fastestPath = np.min([ind.fitness.values[1] for ind in population if ind.fitness.values[0] == 0])
            if fastestPath == lastPath: count += 1
            lastPath = fastestPath       
        iterations += 1
        endTime = time.time() - startTime

    winners = list(filter(lambda pop: pop.fitness.values[0] == 0, population))

    if winners and len(winners)!=0:
        #result = the winner if he is alone or the shortest  
        finalResult = winners[0] if len(winners) == 1 else list(reduce(lambda ind1, ind2: ind1 if len(getChromosomePath(ind1)) < len(getChromosomePath(ind2)) else ind2, winners))
    else:
        #result = the best path found if doesn't find the path
        finalResult = population[np.argmin(np.array([ind.fitness.values[0] for ind in population]))]
        print("No winner found, show the best try")

    print(f"Found in {iterations} iterations\nFound in {endTime}s")
    print(f"MUTPB={MUTPB} and CXPB={CXPB}")
    print(f"Size of the population :  {populationSize}, with {tournoisSize} selectionned per iteration")
    print(f"Length : {len(getChromosomePath(finalResult))}")
    return getChromosomePath(finalResult)