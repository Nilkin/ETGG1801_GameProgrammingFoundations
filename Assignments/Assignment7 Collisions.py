#Assignment 7 Collisions
#Etgg 1801-02 by. Thomas Gilman

#imports
import random
import time
import pscreen

#Time
startTime = time.time()
endTime = startTime+60

#load screen

pscreen.loadScreen()

#color values
randR=random.randint(5,250)
randG=random.randint(5,250)
randB=random.randint(5,250)
randC=(randR,randG,randB)
black=(0,0,0)
aWhite=(250,235,215)
white=(255,255,255)
nBlue=(0,0,128)
dGray=(105,105,105)
sGray=(112,138,144)
Gold=(255,215,0)
pGoldr=(238,232,170)
S=(250,128,114)
dS=(233,150,122)
#random x and y
randX=random.randint(25,775)
randY=random.randint(25,575)
#random item location
iX=randX
iY=randY
#player values
pX=350 #player starting x cord
pY=350 #player starting y cord
pR=30 #player radius
iR=30 #item radius
pDx=0
pDy=0
pSpeed=2 #player speed
pIspeed=0 #player initial speed
#object values
tx=randX #item random starting x cord
ty=randY #item random starting y cord
iDx=1
iDy=1
iInitialSpeed=1
#Obstacle values
oX=random.randint(50,750)
oY=random.randint(50,550)
oR=30
#starting score value
s=0
#mood vaule
m=15
#functions
#player function
def drawP():
    #body
    pscreen.circle(pX,pY,pR,aWhite,0)
    #eyes
    pscreen.circle(int(pX)-15,int(pY)-12,pR-20,white,0)
    pscreen.circle(int(pX)+15,int(pY)-12,pR-20,white,0)
    #eye color
    pscreen.circle(int(pX)-15,int(pY)-12,pR-25,nBlue,0)
    pscreen.circle(int(pX)+15,int(pY)-12,pR-25,nBlue,0)
    #pupils
    pscreen.circle(int(pX)-15,int(pY)-12,pR-27,black,0)
    pscreen.circle(int(pX)+15,int(pY)-12,pR-27,black,0)
    #Mouth
    pscreen.line(int(pX)-15,int(pY)+15,(pX)+15,pY+15,black,3)
    pscreen.line(int(pX)-15,int(pY)+15,(pX)-20,pY+m,black,3)
    pscreen.line(int(pX)+15,int(pY)+15,(pX)+20,pY+m,black,3)
    #Nose
    pscreen.circle(pX,pY,pR-25,S,0)
    pscreen.circle(pX,pY,pR-27,dS,0)

#object Function
#supposed to draw a bed because the student is exauhsted
def drawI(iX,iY):
    pscreen.circle(iX,iY,random.randint(30,33),black,0)
    pscreen.circle(iX,iY,iR,Gold,0)
    pscreen.rectangle(iX-25,iY-25,iX+25,iY+25,black,0)
    pscreen.circle(iX,iY,random.randint(15,25),Gold,0)
    pscreen.rectangle(iX-12,iY-12,iX+12,iY+12,pGoldr,0)
    pscreen.circle(iX,iY,random.randint(8,12),Gold,0)
    pscreen.rectangle(iX-6,iY-6,iX+6,iY+6,black,0)
    pscreen.circle(iX,iY,random.randint(4,6),Gold,0)
    pscreen.rectangle(iX-3,iY-3,iX+3,iY+3,pGoldr,0)
    pscreen.circle(iX,iY,random.randint(1,3),Gold,0)
    pscreen.rectangle(iX-1,iY-1,iX+1,iY+1,black,0)
    pscreen.circle(iX,iY,1,Gold,0)

#Background Function
#Draws a background
def drawBackground():
    pscreen.rectangle(0,0,799,799,randC,0)
    pscreen.circle(300,300,200,(178,34,34),0)
    pscreen.circle(300,300,100,(178,40,40),0)

#Time Function
def gameTime():
    timeLeft=endTime-time.time()
    timeLeft=int(timeLeft*10)/10
    pscreen.fontSelect("Arial",20)
    pscreen.fontWrite(5,5,"time:"+str(timeLeft),black)

#Score Function
def keepScore():
    pscreen.fontSelect("Arial",25)
    pscreen.fontWrite(5,570,"score is:"+str(s),black)

#Game over Function
def gameOver():
    pscreen.fontSelect("Arial",50)
    pscreen.fontWrite(290,300,"GAME OVER",black)
    pscreen.fontWrite(290,360,"Score:"+str(s),black)

#Obstacle Function
def drawObstacle():
    pscreen.circle(oX,oY,oR,black,0)
    pscreen.circle(oX,oY,oR-10,dS,0)

#Game loop
while True:
    #second change of cord for item after its picked up
    randX2=random.randint(25,775)
    randY2=random.randint(25,575)
    #escape program
    if pscreen.keyIsPressed("escape"):
        break
    #borders and binding to screen along with bounce back
    if pX<=0 or pX>=799:
        pDx*=-1
    if pY<=0 or pY>=599:
        pDy*=-1
    if pX<=0:
        pX=0
    if pX>=799:
        pX=799
    if pY<=0:
        pY=0
    if pY>=599:
        pY=599
    #keeps item from leaving the screen
    if iX>775:
        iX=775
    if iY>575:
        iY=575
    if iX<0:
        iX=0
    if iY<0:
        iY=0
    #call functions
    drawBackground()
    drawI(iX,iY)
    drawObstacle()
    drawP()
    keepScore()
    gameTime()
    #update position allows player and item to move around
    pX+=pDx
    pY+=pDy
    iX+=iDx
    iY+=iDy
    #movement
    if pscreen.keyIsPressed("a"):
        pDx=-pSpeed
    if pscreen.keyIsPressed("d"):
        pDx=pSpeed
    if pscreen.keyIsPressed("w"):
        pDy=-pSpeed
    if pscreen.keyIsPressed("s"):
        pDy=pSpeed
    #bounce the object off the walls
    if iX<=25 or iX>=775:
        iDx*=-1
    if iY<=25 or iY>=575:
        iDy*=-1
    #distance calc
    distance=((iX-pX)**2+(iY-pY)**2)**float(0.5)
    distance1=((iX-oX)**2+(iY-oY)**2)**float(0.5)
    distance2=((oX-pX)**2+(oY-pY)**2)**float(0.5)
    #checks for collision
    if distance2 <= oR+pR:
        pDx*=-1
        pDy*=-1
    if distance1 <= oR+iR:
        iDx*=-1
        iDy*=-1
    if distance <= pR+iR:
        iX=randX2
        iY=randX2
        s+=1
    #changes facial expression based on radius to object
    if distance < pR+iR+80:
        m=10
    elif distance > pR+iR+80:
        m=20
    #counts down the time
    timeLeft=endTime-time.time()
    if timeLeft <= 0:
        gameOver()
        pscreen.updateScreen()
        time.sleep(5)
        break
        
    #update screen
    pscreen.updateScreen()
#unload Screen
pscreen.unloadScreen()
    
