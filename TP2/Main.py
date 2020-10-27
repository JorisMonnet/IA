from City_Links import *
from aStar import *
import os

if __name__ == "__main__":
    srcCity = ""
    destCity = ""
    heuristic=-1
    dicCity = readAll()
    listCity = [key for key in dicCity.keys()]

    os.system('cls' if os.name=='nt' else 'clear')      #cls
    #cityA,cityB for aStar Algortihm
    print("---------------------------Cities--------------------------------")
    print (listCity)
    print("-----------------------------------------------------------------\n")
    while srcCity not in listCity:
        srcCity = input("Write the source City : ")
    while destCity not in listCity:
        destCity = input("\nWrite the destination City : ")
    
    #Heuristics
    print("\n---------------------------Heuristics----------------------------")
    print("0 : h0(n) = 0")
    print("1 : h1(n) = Distance between n and B on x axis")
    print("2 : h2(n) = Distance between n and B on y axis")
    print("3 : h3(n) = Distance between n and B as the crow flies")
    print("4 : h4(n) = Manhattan Distance between n and B")
    print("-----------------------------------------------------------------\n")
    while heuristic not in ["0","1","2","3","4"]:
        heuristic = input("Write the Heuristic you want to use (0,1,2,3,4) : ")
    
    #Algorithm
    path,steps = aStarAlgorithm(dicCity,dicCity[srcCity],dicCity[destCity],dicHeuristics[heuristic])

    os.system('cls' if os.name=='nt' else 'clear')      #cls
    #Result
    print(f"Path : {srcCity} -> {destCity} found in {steps} steps")
    print("-----------------------------------------------------------------")
    print("START")
    print("-----------------------------------------------------------------")
    parent=path.parent
    listPathCity=[destCity]
    while parent:
        listPathCity.insert(0,str(parent))
        parent=parent.parent
    for city in listPathCity:
        print(f"- {city}")
    print("-----------------------------------------------------------------")
    print("END")
    print("-----------------------------------------------------------------")

