class City :
    def __init__(self,name,x,y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.links = []
        self.parent = None
        
    def __str__(self):
        return self.name

    def __lt__(self,other):
        return True

    def createLinks(self,link):
        self.links.append(link)

    def getNeighbourLeafs(self,dicCity):
        """ return a list of the neighbour leafs"""
        return [dicCity[str(link.destination)] for link in self.links]

    def getWeightOf(self,destination):
        """ return the weight to a leaf"""
        for link in self.links:
            if str(link.destination)==str(destination.name):
                return int(str(link.weight))
        
class Links:
    def __init__(self,destination,weight):
        self.destination=destination
        self.weight=weight

def readCityFile(dicCity):
    file=open("positions.txt","r")
    for linePos in file:
        name,x,y=linePos.split()
        dicCity[name]=City(name,x,y)

def readLinksFile(dicCity):
    file=open("connections.txt","r")
    for lineCon in file:
        src,dst,weight=lineCon.split()
        try:
            dicCity[src].createLinks(Links(dicCity[dst],weight))
            dicCity[dst].createLinks(Links(dicCity[src],weight))
        except:
            print("error in file")

def readAll():
    dicCity={}
    readCityFile(dicCity)
    readLinksFile(dicCity)
    return dicCity