from taquin_viewer import TaquinViewerHTML
from state_modele import State
from play import search
    
if __name__ == '__main__':

    # You should test the following initial configurations:
    # your algorithm should reach the solution in few iterations
    taquin_easy = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    # your algorithm should reach the solution in few hundred iterations
    taquin_medium = [
        [0, 1, 2],
        [7, 4, 3],
        [5, 8, 6]
    ]

    # your algorithm will need more then 100'000 iterations
    taquin_hard = [
        [4, 0, 2],
        [3, 5, 1],
        [6, 7, 8]
    ]

    # just impossible
    taquin_impossible = [
        [1, 2, 3],
        [4, 5, 6],
        [8, 7, 0]
    ]

    currentState = search(State(taquin_medium))
    statesPath = []
    while currentState.parent is not None :
        statesPath.insert(0, currentState)
        currentState = currentState.parent
    statesPath.insert(0, currentState)

    i = 1
    with TaquinViewerHTML() as viewer:
        for board in statesPath:
            viewer.add_taquin_state(board.values, "move" + str(i))
            i = i+1