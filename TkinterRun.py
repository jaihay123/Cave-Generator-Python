import sys
import os
import tkinter
import pygame

from CaveGenerator import *
from FileManager import *

class Program(object):
    
    def __init__(self, root, d ,mn, mx):
        #Sets a tkinter instance
        self.root = root
        self.root.title("Cellular Automata v0.5")
        #set the weights of the grid
        self.root.grid_rowconfigure(0, weight=1) 
        self.root.grid_columnconfigure(0, weight=1) 
        self.root.grid_columnconfigure(1, weight=1) 
        #Gets the screen resolution
        self.width = 600
        self.height = 500
        #Gets the values for the cave
        self.density = d
        self.mn = mn
        self.mx = mx
        #Create frame for the pygame window to go in
        self.pyframe = tkinter.Frame(self.root, width=self.width - 100, height=self.height)
        #Create frame for the cave settings
        self.setframe = tkinter.Frame(self.root, width=100, height=self.height) #added
        #Creates a top menu bar
        self.menubar = tkinter.Menu(self.root)
        #Creates a dropdown box from the menu
        self.filemenu = tkinter.Menu(self.menubar, tearoff=0)
        #Creates an Open and Save button in the dropdown
        self.filemenu.add_command(label="Open", command=self.LoadCave)
        self.filemenu.add_command(label="Save", command=self.SaveCave)
        self.filemenu.add_separator()
        #Label the dropdown as File
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.root.config(menu=self.menubar)
        #Create the button label
        self.buttonlabel = tkinter.Label(self.setframe, text="Cave Density")
        #Create the button to generate the cave
        self.button = tkinter.Button(self.setframe, text="Generate", command=self.Generate, height = 2, width = 8)
        #Create the slider
        self.slider = tkinter.Scale(self.setframe, from_=0, to=25, orient=tkinter.HORIZONTAL)
        
        #Put the objects in the right location
        self.pyframe.grid(row=0, column=0)
        self.setframe.grid(row=0, column=1, rowspan=2)
        self.buttonlabel.grid(row=2, column=1)
        self.slider.grid(row=3, column=1, sticky="ew")
        self.button.grid(row=4, column=1, sticky="ew")
        
        #Update to display
        self.root.update()
        ###Tkinter Done###
        
        #The three lines below embed a pygame window to a tkinter window
        os.environ['SDL_WINDOWID'] = str(self.pyframe.winfo_id())
        if sys.platform == "win32":
            os.environ['SDL_VIDEODRIVER'] = 'windib'

        #Initialize Pygame
        pygame.display.init()
        #Set the screen size
        self.screen = pygame.display.set_mode((self.width, self.height))
        ###Pygame Done###
                
    def Generate(self):
        #Create a new cave
        self.cave = Cave(self.height,self.width,(float(self.slider.get()) * 0.1),self.mn,self.mx)
        #Generate the cave
        self.cave.Generate()
        #Get the cave data
        self.pixels = self.cave.Render()
        #Run the render loop
        self.loop()
        
        
          
    def loop(self):
        #Fill the screen black
        self.screen.fill((0,0,0))
        #Create a pixel
        square=pygame.Surface((1, 1)) #changed
        #loop through the positions
        for x in range(0, self.width, 1):
            for y in range(0, self.height, 1):
                #Check if a pixel needs to be displayed at position
                if self.pixels[y][x] == 1:
                    #Fill the colour white
                    square.fill((255,255,255))
                    draw_me=pygame.Rect((x+1), (y+1), 1, 1)
                    self.screen.blit(square,draw_me)
        #Update the screen to render
        pygame.display.flip()
        #self.pyframe.after(5, self.loop)

    def SaveCave(self):
        #Open a save file box and let the user save it in a location of choice
        savename = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".cave")
        #Check if cancel button has been pressed. If so return
        if savename is None: 
            return
        #Runs the default classes to save
        filem = CFile(savename, self.cave)
        filem.WriteData()
        filem.SaveCreateFile()

    def LoadCave(self):
        #Open a load file box and let the user save it in a location of choice
        loadname = tkinter.filedialog.askopenfile(mode='r', defaultextension=".cave")
        #Check if cancel button has been pressed. If so return
        if loadname is None:
            return
        #Runs the default classes to load
        parser = ParseCFile(loadname)
        parser.ReadFile()
        self.cave = parser.Parse()
        #Gets the data for the pixel display
        self.pixels = self.cave.Render()
    

if __name__ == "__main__":
    #Creates the tkinter instance
    root = tkinter.Tk()
    #Creates a Program instance
    program = Program(root, 0.8, 1, 2) #0.8 is not needed anymore because self.density is not used.
    #Loop tkinter
    root.mainloop()
   
            
    
