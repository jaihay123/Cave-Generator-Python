#Written By Jaime Haynes
#Example Use

from CaveGenerator import *
from FileManager import *


def CreateCave():
    w = int(input("Please enter the width in integer: "))
    h = int(input("Please enter the height in integer: "))
    d = float(input("Please enter the amount of cave generation in float: "))
    mn = 0
    mx = 2
    cave = Cave(h, w, d, mn, mx)
    return cave
        
def GenerateCave(cave):
    r = int(input("Please enter the iterations in integer: "))
    for i in range(r):
        cave.Generate()
        print("Stage " + str(i + 1))
        print(cave.Display())
        print()
        print()

def SaveCave(cave):
    savename = str(input("Please enter the save file name: "))
    filem = CFile(savename, cave)
    filem.WriteData()
    filem.SaveCreateFile()
    
def LoadCave():
    loadname = str(input("Please enter the file name to load: "))
    parser = ParseCFile(loadname)
    parser.ReadFile()
    cave = parser.Parse()
    return cave

def SaveSnap(cave):
    filename = str(input("Please enter the snap name: "))
    snap = SnapFile(filename, cave.Display())
    snap.SaveSnap()


cave = None
print("Cave Generator v0.3")
while True:
    print()
    print()
    print("1 - Create Cave")
    print("2 - Generate Cave")
    print("3 - Save Cave")
    print("4 - Load Cave")
    print("5 - Display Cave")
    print("6 - Save Display")
    print("7 - Discard Cave")
    print()
    inp = int(input("Please enter choice: "))

    if inp == 1:
        cave = CreateCave()
    if inp == 4:
        cave = LoadCave()
    if cave != None:
        if inp == 2:
            GenerateCave(cave)
        elif inp == 3:
            SaveCave(cave)
        elif inp == 5:
            print()
            print(cave.Display())
            print()
        elif inp == 6:
            SaveSnap(cave)
        elif inp == 7:
            cave = None
    else:
        print("You haven't created a cave file yet.")
    

    
    
    












    
