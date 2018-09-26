#Functions and Game Loop, Assignment 6 Program 1
#by. Thomas Gilman ETGG 1801-02

#imports for code
import pscreen
import math
import random
import time

#loading process
pscreen.loadScreen()
pscreen.fontSelect("Arial",24)

#Global random colors for randomness in all colors
#randR=Red
randR = random.randint(5,250)
#randG=Green
randG = random.randint(5,250)
#randB=Blue
randB = random.randint(5,250)
#random Color
randColor=(randR,randG,randB)
#random x
rand_x = random.randint(25,744)
#random y
rand_y = random.randint(25,744)
#mood
m1=["happy","nuetral","mad"]
randMood=m1[random.randint(0,len(m1)-1)]
#i value for multiple faces
i=0

#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
brown=(139,69,19)
yellow=(255,255,0)
aWhite=(250,235,215)
randR=random.randint(10,245)
randG=random.randint(10,245)
randB=random.randint(10,245)
randColor=(randR,randG,randB)

#Functions

#Function 1, drawBorderBox function
def drawBorderBox():
    #defining boxColor for color of border
    boxColor=(randR,randG,randB)
    #rectangles' that make up border
    pscreen.rectangle(0,0,20,799,boxColor,0)
    pscreen.rectangle(0,0,799,20,boxColor,0)
    pscreen.rectangle(799,0,779,799,boxColor,0)
    pscreen.rectangle(0,579,799,799,boxColor,0)

#Function 2 draw face
def drawFace(x,y):
    #assigning values
    #Head
    pscreen.circle(x,y,25,aWhite,0)
    #mouth
    pscreen.line(x-5,y+5,x+5,y+5,black,)
    pscreen.line(x-5,y+5,x-7,y+2,black,0)
    pscreen.line(x+5,y+5,x+7,y+2,black,0)
    #eyes
    pscreen.ellipse(x-5,y-10,4,4,white,0)
    pscreen.ellipse(x+5,y-10,4,4,white,0)
    pscreen.circle(x-5,y-10,2,blue,0)
    pscreen.circle(x+5,y-10,2,blue,0)
    #nose
    pscreen.line(x-2,y+2,x,y-1,black,0)
    pscreen.line(x-2,y+2,x+1,y+1,black,0)

#Function 3 draw some treasures
def drawTreasure(x,y):
    #chest1
    #chest top
    pscreen.rectangle(x-50,y-50,x-40,y-20,brown,0)
    pscreen.triangle(x-50,y-50,x-50,y-20,x-60,y-20,brown,0)
    pscreen.triangle(x-40,y-20,x-40,y-50,x-30,y-20,brown,0)
    #chest body
    pscreen.rectangle(x-60,y-20,x-30,y,brown,0)
    #line between chest lid and chest body
    pscreen.line(x-50,y-20,x-40,y-20,black,0)
    #chest lock
    pscreen.rectangle(x-47,y-23,x-42,y-14,yellow,0)
    
#Program 1 game loop
while True:
   
    drawFace(400,400)
    drawTreasure(300,200)
    drawTreasure(600,200)
    drawTreasure(700,400)
    drawBorderBox()
    pscreen.fontWrite(0,0,"press:Escape to exit program 1.",(255,255,255))
    #update Screen
    pscreen.updateScreen()
    if pscreen.keyIsPressed("escape"):
        break
    
#second drawFace for program 2
def drawFace2(x,y,randColor,randMood):
    #Head
    pscreen.circle(x,y,25,randColor,0)
    #mouth
    if randMood == "happy":#happy face
        pscreen.line(x-5,y+5,x+5,y+5,black)
        pscreen.line(x-5,y+5,x-7,y+2,black,0)
        pscreen.line(x+5,y+5,x+7,y+2,black,0)
    if randMood == "mad":#mad face
        pscreen.line(x-5,y+5,x+5,y+5,black)
        pscreen.line(x-5,y+5,x-7,y+7,black,0)
        pscreen.line(x+5,y+5,x+7,y+7,black,0)
    if randMood == "nuetral":#nuetral face
        pscreen.line(x-5,y+5,x+5,y+5,black)
    #eyes
    if randMood == "happy":
        pscreen.ellipse(x-5,y-10,4,4,white,0)
        pscreen.ellipse(x+5,y-10,4,4,white,0)
        pscreen.circle(x-5,y-10,2,blue,0)
        pscreen.circle(x+5,y-10,2,blue,0)
    if randMood == "nuetral":
        pscreen.ellipse(x-5,y-10,4,4,white,0)
        pscreen.ellipse(x+5,y-10,4,4,white,0)
        pscreen.circle(x-5,y-10,2,blue,0)
        pscreen.circle(x+5,y-10,2,blue,0)
    if randMood == "mad":
        pscreen.line(x-10,y-18,x-5,y-15,black)
        pscreen.line(x+10,y-18,x+5,y-15,black)
        pscreen.ellipse(x-5,y-10,4,4,white,0)
        pscreen.ellipse(x+5,y-10,4,4,white,0)
        pscreen.circle(x-5,y-10,2,blue,0)
        pscreen.circle(x+5,y-10,2,blue,0)
    #nose
    pscreen.line(x-2,y+2,x,y-1,black,0)
    pscreen.line(x-2,y+2,x+1,y+1,black,0)

#update screen 2
pscreen.clearScreen(black)
pscreen.updateScreen()

#Program 2 game loop
while True:
    drawBorderBox()
    pscreen.fontWrite(0,0,"press:Q to exit program 2 after program.",(255,255,255))
    while i<10:
        #program 2 random face values
        randMood2=m1[random.randint(0,len(m1)-1)]
        rand_x2=random.randint(25,700)
        rand_y2=random.randint(25,544)
        randR2=random.randint(5,250)
        randG2=random.randint(5,250)
        randB2=random.randint(5,250)
        randColor2=(randR2,randG2,randB2)
        #program 2 random color values for only program 2
        #draw 10 random moody faces and colors
        drawFace2(rand_x2,rand_y2,randColor2,randMood2)
        i+=1
        pscreen.updateScreen()
    pscreen.updateScreen()
    if pscreen.keyIsPressed("q"):
        break

#unload screen
pscreen.unloadScreen()

