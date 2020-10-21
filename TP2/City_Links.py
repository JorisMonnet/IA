class City :
    self.links = []
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
    def __str__(self):
        return self.name
    def createLinks(self,link):
        self.links.append(link)
        
class Links:
    def __init__(self,destination,weight):
        self.destination=destination
        self.weight=weight