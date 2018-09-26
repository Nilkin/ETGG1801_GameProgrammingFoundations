#Final Exam program, problem 18
#Thomas Gilman
#Paul Yost
#Etgg 1801-02
#16 December, 2015

#imports
import pscreen
import math
import time


#load Screen
pscreen.loadScreen()

#draw function
def drawArrow(base_x=300,base_y=400,angle=0):
    #values
    x=base_x
    y=base_y
    #base
    p1x=x+25*math.cos(math.radians(angle+45))
    p1y=y-10*math.sin(math.radians(angle+45))
    p2x=x+25*math.cos(math.radians(angle-45))
    p2y=y+10*math.sin(math.radians(angle-45))
    p3x=x-25*math.cos(math.radians(angle+135))
    p3y=y-10*math.sin(math.radians(angle+135))
    p4x=x-25*math.cos(math.radians(angle-135))
    p4y=y+10*math.sin(math.radians(angle-135))
    #head
    h1x=x+25*math.cos(math.radians(angle))
    h1y=y-15*math.sin(math.radians(angle))
    h2x=x+75*math.cos(math.radians(angle+90))
    h2y=y*math.sin(math.radians(angle+90))
    h3x=x+25*math.cos(math.radians(angle-90))
    h3y=y+15*math.sin(math.radians(angle-90))
    #draw the arrow
    pscreen.triangle(h1x,h1y,h2x,h2y,h3x,h3y,(255,0,0),0)
    pscreen.triangle(p1x,p1y,p2x,p2y,p4x,p4y,(255,0,0),0)
    pscreen.triangle(p2x,p2y,p3x,p3y,p4x,p4y,(255,0,0),0)
angle=0
while True:
    pscreen.clearScreen((0,0,0))
    if pscreen.keyIsPressed("escape"):
        break
    drawArrow(300,400,angle)
    if pscreen.keyIsPressed("d"):
        angle-=5
    if pscreen.keyIsPressed("a"):
        angle+=5
    pscreen.updateScreen()
pscreen.unloadScreen()
        
    
    
    
    
