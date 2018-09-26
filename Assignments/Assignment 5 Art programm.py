#pscreen Art programm
#Assignment 5 by. Thomas Gilman ETGG 1801-02

#imports for code
import pscreen
import math
import random
import time

#loading process
pscreen.loadScreen()

brush_radius=5
brush_color=(255,255,255)
isCircle=True
pscreen.fontSelect("Arial",24)

#Game Loop
while True:
    #input
    x=pscreen.mouseGetX()
    y=pscreen.mouseGetY()
    #random color values for F1 button
    rand_x = random.randint(0,255)
    rand_y = random.randint(0,255)
    rand_z = random.randint(0,255)
    #screen refresh
    pscreen.updateScreen()
    #loop break
    if pscreen.keyIsPressed("q"):
        break
    #mouse button brush's
    if pscreen.mouseGetButtonR():
        if isCircle:
            pscreen.circle(x,y,brush_radius,(0,0,0),0)
        else:
            pscreen.rectangle(x,y,x-brush_radius,y-brush_radius,(0,0,0),0)
    if pscreen.mouseGetButtonL():
        if isCircle:
            pscreen.circle(x,y,brush_radius,brush_color,0)
        else:
            pscreen.rectangle(x,y,x-brush_radius,y-brush_radius,brush_color,0)
#Clear Screen
    if pscreen.keyIsPressed("c"):
        pscreen.clearScreen((0,0,0))
    

#Boarders where you cant leave program
    if x<0:
        x=0
    if x>799:
        x=799
    if y<0:
        y=0
    if y>799:
        y=799
    #Values for color, radius, and brush shape
    if pscreen.keyIsPressed("w"):
        brush_color=(255,255,255)
    if pscreen.keyIsPressed("r"):
        brush_color=(255,0,0)
    if pscreen.keyIsPressed("g"):
        brush_color=(0,255,0)
    if pscreen.keyIsPressed("b"):
        brush_color=(0,0,255)
    if pscreen.keyIsPressed("1"):
        brush_radius=5
    if pscreen.keyIsPressed("2"):
        brush_radius=10
    if pscreen.keyIsPressed("3"):
        brush_radius=20
    if pscreen.keyIsPressed("f1"):
        brush_color=(rand_x,rand_y,rand_z)
    if pscreen.keyIsPressed("9"):
        isCircle=False
    if pscreen.keyIsPressed("8"):
        isCircle=True
    #Exit button and bar with tools
    pscreen.rectangle(0,540,799,799,(255,255,0),0)#box containing Exit button
    pscreen.circle(80,570,5,(0,0,0),0)#small radius
    pscreen.circle(110,570,10,(0,0,0),0)#medium radius
    pscreen.circle(150,570,20,(0,0,0),0)#large radius
    pscreen.rectangle(180,565,190,575,(0,0,0),0)#rectangle for brush shape
    #colors
    pscreen.rectangle(200,565,210,575,(0,0,0),0)#black color
    pscreen.rectangle(200,575,210,585,(255,255,255),0)#white color
    pscreen.rectangle(210,565,220,575,(255,0,0),0)#Red color
    pscreen.rectangle(210,575,220,585,(0,255,0),0)#Green color
    pscreen.rectangle(220,565,230,575,(0,0,255),0)#Blue color
    pscreen.rectangle(220,575,230,585,(255,255,0),0)#Red, and Green color
    pscreen.rectangle(230,565,240,575,(255,0,255),0)#Red,and Blue color
    pscreen.rectangle(230,575,240,585,(0,255,255),0)#Blue,and Green color
    #exit button
    pscreen.rectangle(70,547,15,580,(255,255,255),0)#box under exit button
    pscreen.fontWrite(25,550,"Exit",(255,0,255))#should display Exit in the bottom left corner
    #Exit button loop break
    if pscreen.mouseGetButtonL()and 15<x<70 and 547<y<580:
        break
    #objects that change brush size, and shape
    if pscreen.mouseGetButtonL()and 75<x<85 and 565<y<575:
        brush_radius=5
        isCircle=True
    if pscreen.mouseGetButtonL()and 100<x<120 and 565<y<575:
        brush_radius=10
        isCircle=True
    if pscreen.mouseGetButtonL()and 130<x<170 and 565<y<575:
        brush_radius=20
        isCircle=True
    if pscreen.mouseGetButtonL()and 180<x<190 and 565<y<575:
        isCircle=False
    #change colors
    if pscreen.mouseGetButtonL()and 200<x<210 and 565<y<575:
        brush_color=(0,0,0)
    if pscreen.mouseGetButtonL()and 200<x<210 and 575<y<585:
        brush_color=(255,255,255)
    if pscreen.mouseGetButtonL()and 210<x<220 and 565<y<575:
        brush_color=(255,0,0)
    if pscreen.mouseGetButtonL()and 210<x<220 and 575<y<585:
        brush_color=(0,255,0)
    if pscreen.mouseGetButtonL()and 220<x<230 and 565<y<575:
        brush_color=(0,0,255)
    if pscreen.mouseGetButtonL()and 220<x<230 and 575<y<585:
        brush_color=(255,255,0)
    if pscreen.mouseGetButtonL()and 230<x<240 and 565<y<575:
        brush_color=(255,0,255)
    if pscreen.mouseGetButtonL()and 230<x<240 and 575<y<585:
        brush_color=(0,255,255)

#Infinite loop
pscreen.updateScreen()

#End Process
pscreen.unloadScreen()



   


