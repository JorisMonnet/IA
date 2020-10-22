class City :
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
        self.links = []
        
    def __str__(self):
        return self.name

    def createLinks(self,link):
        self.links.append(link)
    def getPos(self):
        return (self.x,self.y)
        
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