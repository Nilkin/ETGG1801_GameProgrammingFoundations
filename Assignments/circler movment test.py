#Game loop test example code

#Initialization
import pscreen
import time

playerX = 400
playerY = 300

pscreen.loadScreen()
pscreen.fontSelect("Arial",24)

#Game Loop
while True:
    #input
    if pscreen.keyIsPressed("q"):
        break
    if pscreen.keyIsPressed("a"):
        playerX-=1
    if pscreen.keyIsPressed("d"):
        playerX+=1
    if pscreen.keyIsPressed("w"):
        playerY-=1
    if pscreen.keyIsPressed("s"):
        playerY+=1
    #contain player on the screen
    if playerX<0:
        playerX=0
    if playerX>799:
        playerX=799
    if playerY<0:
        playerY=0
    if playerY>599:
        playerY=599
   
    #render objects / draw stuff
    #clear the screen
    pscreen.clearScreen((0,0,0))
    #draw a circle
    pscreen.circle(playerX,playerY,20,(255,255,0),0) #head outline
    pscreen.circle(playerX-6,playerY-6,3)#left eye (our left)
    pscreen.circle(playerX-6,playerY-6,2,(0,255,255),0)#left pupil
    pscreen.circle(playerX+6,playerY-6,3)#right eye (our right)
    pscreen.circle(playerX+6,playerY-6,2,(0,255,255),0)#right pupil
    pscreen.line(playerX-8,playerY+8,playerX+8,playerY+8,(255,0,255))#mouth
    
    pscreen.fontWrite(0,0,"Game Loop Example",(255,255,255))#display text in upper left hand corner (our left) 
    pscreen.updateScreen()

#Clean-up
pscreen.unloadScreen()
