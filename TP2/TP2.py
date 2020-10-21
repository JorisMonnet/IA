def read(name):
    file=open(name,"r")
    return [line for line in file]
def readPositions(nodeList):
    lineList = read("positions.txt")
    for line in lineList:
        line.split
def readConnections(connectionsList):
    pass
def aStar_algo(villeA,villeB,heuristic):
    
    frontiere  = [start]
    history = []
    start=0
    end=0
    while len(frontiere)>0:
        frontiere.sort
        current = frontiere.pop(0)
        history.append(current)
        if current == end:
            path=[]
            while current != start:
                path.append

if __name__ == "__main__":
    pass