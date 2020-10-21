import City_Links
def readPositions(listCity):
    file=open("positions.txt","r")
    for linePos in file:
        name,x,y=linePos.split()
        listCity.append(City_Links.City(name,x,y))

def readConnections(listCity):
    file=open("connections.txt","r")
    for lineCon in file:
        src,dst,weight=lineCon.split()
        for city in listCity:
            if src==city.name:
                city.createLinks(City_Links.Links(dst,weight))

if __name__ == "__main__":
    listCity=[]
    readPositions(listCity)
    readConnections(listCity)
    for city in listCity:
        print(city)
