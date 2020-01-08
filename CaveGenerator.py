#Cave Generator v0.3
#Written By Jaime Haynes

import random

class Cave():

    def __init__(self, h, w, d, mn, mx):
        self.h = h #width
        self.w = w #height
        self.d = d #density
        self.space = [[0 for a in range(w)] for b in range(h)] #2D Array representing space
        self.display = "" #display string. Just for version 1
        self.min = mn #minimum 
        self.max = mx #maximum
        #Populate the Array
        for x in range(self.h):
            for y in range (self.w):
                self.space[x][y] = 0
                
    def Generate(self):
        #Empty the string
        self.display = ""
        #Work out the seeds
        for x in range(self.h):
            for y in range (self.w):
                if random.uniform(0.0, 100) < self.d:
                    self.space[x][y] = 1
                

        #Expand the seeds depending on the density
        for x in range(self.max, self.h - self.max, 1):
            for y in range (self.max, self.w - self.max, 1):
                if self.space[x][y] == 1:
                    for xa in range(x, x + random.randint(self.min, self.max), 1):
                        for ya in range (y, y + random.randint(self.min, self.max), 1):
                            self.space[xa][ya] = 1
                    for xb in range(x, x - random.randint(self.min, self.max), -1):
                        for yb in range (y, y - random.randint(self.min, self.max), -1):
                            self.space[xb][yb] = 1
                            
        #Check for odd parts
        for x in range(1, (self.h) - 1, 1):
            for y in range (1, self.w - 1, 1):
                if self.space[x][y] == 0:
                    if self.space[x + 1][y] == 1 and self.space[x - 1][y] == 1:
                        self.space[x][y] = 1
                    if self.space[x][y + 1] == 1 and self.space[x][y - 1] == 1:
                        self.space[x][y] = 1
        
    def Display(self):
        #Create a string of the caves and return it
        reader = ""
        for x in range(self.h):
            for y in range (self.w):
                if self.space[x][y] == 1:
                    reader = reader + "."
                else:
                    reader = reader + "#" #+ str(self.space[x][y])
            self.display = self.display + "\n" + reader
            reader = ""
        return self.display

    def Render(self):
        return self.space

    def setPixel(self, x, y, size, screen):
        for i in range(x, x + size, 1):
            for j in range(y, y + size, 1):
                screen.set_at((i, j), (255,255,255))


    def setData(self, data):
        self.space = data
        
            
