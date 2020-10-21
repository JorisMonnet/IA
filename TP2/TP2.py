import City_Links

def read(name):
    file=open(name,"r")
    return [line for line in file]

def readPositions(listCity):
    lineList = read("positions.txt")
    for line in lineList:
        name,x,y=line.split()
        listCity.append(City_Links.City(name,x,y))

def readConnections(listCity):
    lineList = read("connections.txt")
    for line in lineList:
        src,dst,weight=line.split()
        for city in listCity:
            if src==city:
                city.addLink(City_Links.Links(dst,weight))

if __name__ == "__main__":
    listCity=[]
    readPositions(listCity)
    readConnections(listCity)
    for city in listCity:
        print(city)
