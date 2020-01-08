import pygame, sys, os
from CaveGenerator import *
import tkinter







def Generate(w,h,d,mn,mx):
    cave = Cave(h, w, d, mn, mx)
    cave.Generate()
    return cave

def run(screen, cave, cstart):
    screen.fill((0,0,0))
    pixels = cave.Render()
    for y in range(cave.w):
        for x in range(cave.h):
            if pixels[x][y] == 1:
                cave.setPixel(y,x,1, screen)
    pygame.display.flip()




cstart = 0
root = tkinter.Tk()
frame = tkinter.Frame(root, width=500, height=500)
frame.grid(row=0, columnspan=2)
frame.pack()
w = tkinter.Button(root, text="->", callback=)
w.grid(row=1, column=0)
w.pack()
root.update()
os.environ['SDL_WINDOWID'] = str(frame.winfo_id())
if sys.platform == "win32":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((500,500))
w = 500
h = 500
d = 0.5
mn = 1
mx = 2
cave = Generate(w,h,d,mn,mx)
run(screen, cave)
root.mainloop()
   
            
    
