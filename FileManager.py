from CaveGenerator import *

class CFile():

    def __init__(self, filename, cave):
        self.filename = filename
        self.data = ""
        self.cave = cave
        
    def SaveCreateFile(self):
        cfile = self.filename
        cfile.write(self.data)
        cfile.close()

    def WriteData(self):
        self.CaveParse()
        newData = ""
        newData = newData + str(self.cave.h) + " | " + str(self.cave.w) + " | " + str(self.cave.d)
        newData = newData + "\n" + self.data
        self.data = newData

    def CaveParse(self):
        #Create a string of the caves and return it
        reader = ""
        for x in range(self.cave.h):
            for y in range (self.cave.w):
                reader = reader + str(self.cave.space[x][y])
            self.data = self.data + "\n" + reader
            reader = ""
            
class SnapFile():

    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
        
        
    def SaveSnap(self):
        cfile = open("Snaps/" + self.filename + ".txt", "w")
        cfile.write(self.data)
        cfile.close()

    


class ParseCFile():

    def __init__(self, filename):
        self.filename = filename
        self.data = ""
        

    def ReadFile(self):
        cfile = self.filename
        self.data = cfile.read()
        cfile.close()

    def Parse(self):
        tempdata = self.data.replace(" | ", " , ")
        tempdata = tempdata.replace("\n", " , ")
        dataList = tempdata.split(" , ")
        #return dataList
        h = int(dataList[0])
        w = int(dataList[1])
        d = float(dataList[2])
        temp = []
        space = []
        for i in range(4, len(dataList), 1):
            for j in range(len(dataList[i])):
                temp.append(int(dataList[i][j]))
            
            space.append(temp)
            temp = []
        cave = Cave(h,w,d,1,2)
        cave.setData(space)
        return cave

    
        
        
    
    
        
        
