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
            
        for neighbourLeafs in current.getNeighbourLeafs(dicCity):
            tempWeight = totalWeight[current] + current.getWeightOf(neighbourLeafs)
            if neighbourLeafs not in totalWeight or tempWeight < totalWeight[neighbourLeafs]:
                totalWeight[neighbourLeafs] = tempWeight
                neighbourLeafs.parent = current

                priority = h(neighbourLeafs, cityB) + tempWeight
                heapq.heappush(frontier,(priority,neighbourLeafs))

    raise Exception("no solution")