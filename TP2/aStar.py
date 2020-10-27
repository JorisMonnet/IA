import math
import heapq

def h0(n,B): return 0
def h1(n,B): return abs(B.x-n.x)
def h2(n,B): return abs(B.y-n.y)
def h3(n,B): return math.sqrt((B.x-n.x)**2+(B.y+n.y)**2)
def h4(n,B): return h1(n,B)+h2(n,B)

dicHeuristics={"0":h0,"1":h1,"2":h2,"3":h3,"4":h4}

def aStarAlgorithm(dicCity,cityA,cityB,h):
    frontier = []
    heapq.heappush(frontier,(0,cityA))

    totalWeight = {cityA: 0}
    steps = 0

    while frontier:
        current = heapq.heappop(frontier)[1]
        steps+=1

        if current==cityB:
            return current, steps
            
        for neighbourLeaf in current.getNeighbourLeafs(dicCity):
            tempWeight = totalWeight[current] + current.getWeightOf(neighbourLeaf)

            #check for each neighbour Leaf if it come closer to destination or not by changing it's priority in queue if it has not been visited yet 
            #or if the algorithm find a smaller path from source to this leaf
            if neighbourLeaf not in totalWeight or tempWeight < totalWeight[neighbourLeaf]:
                totalWeight[neighbourLeaf] = tempWeight
                neighbourLeaf.parent = current

                priority = h(neighbourLeaf, cityB) + tempWeight #use heuristic to change priority in heapq
                heapq.heappush(frontier,(priority,neighbourLeaf))

    raise Exception("No solution found")