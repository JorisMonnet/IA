from City_Links import readAll
import math
import heapq

def h0(n,B): return 0
def h1(n,B): return B.X-n.X
def h2(n,B): return B.Y-n.Y
def h3(n,B): return math.sqrt((B.X-n.X)**2+(B.Y+n.Y)**2)
def h4(n,B): return h1(n,B)+h2(n,B)

def aStarAlgorithm(cityA,cityB,h,start):
    iteration=1
    frontiere=[cityA.getPos()]
    history=[]

    while frontiere:
            state = heapq.heappop(frontiere)
            history[etat] = state.f
            if state.final(cityB.getPos()):
                return state
            for op in state.applicable_operators():
                new = state.apply(op)
                new.f = cityBlock(new.values) + new.depth
                if new not in history or new.f < history[new]:
                    heapq.heappush(frontiere, new)
            iteration += 1
    raise Exception("No Solution")
    



if __name__ == "__main__":
    dicCity = readAll()


