#Assignment 8 AstroCrash
#ETGG 1801-02 by. Thomas Gilman

#imports
import pscreen
import time
import random

#loadScreen
pscreen.loadScreen()
pscreen.fontSelect('Arial',16)

#Start time
startTime=time.time()
endTime=0

#Color
Green = (0,230,0)
Black = (0,0,0)
White=(255,255,255)

#player start position
pX=400
pY=525
#Population count
pop=2000

#Functions
#distance formula
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
#player module
def drawP():#draws the player
    #main canon body
    pscreen.triangle(pX-5,pY,pX+25,pY,pX+10,pY-30,(245,245,245),0)
    pscreen.rectangle(pX+5,pY,pX+15,pY-10,(105,105,105),0)
    pscreen.circle(pX+10,pY-20,random.randint(1,4),(255,215,0),0)
    
#Ground
def drawG():#draws the ground
    pscreen.rectangle(0,525,799,599,(105,105,105),0)

#starfield background
def drawS():#draws stars
    star_list=[]
    numStars=100
    #random color for stars
    randR=random.randint(0,255)
    randG=random.randint(0,255)
    randB=random.randint(0,255)
    randC=(randR,randG,randB)
    #add stars to list for background
    for i in range(0,numStars):
        star_list.append((random.randint(0,799),random.randint(0,450)))
     #randomize and draw random star locations
    for i in range(0,len(star_list)-1):
        (starX,starY)=star_list[i]
        pscreen.circle(starX,starY,random.randint(1,2),randC,0)

#Asteroid
def Asteroid(Ax,Ay):
    pscreen.circle(Ax,Ay,20,(112,138,144),0)

#Game Time
def gameOver():
    pscreen.fontSelect("Arial",18)
    pscreen.fontWrite(310,300,"GAME OVER")
    pscreen.fontWrite(300,350,"Time Survived:"+str(sTime))
    pscreen.updateScreen()
    time.sleep(5)
#lists
#Bullet list
Bullet_list=[]
bullet_recharge_time=0
#Asteroid list
A_list=[]

#game loop
while True:
    Ax=random.randint(10,789)
    #break statment
    if pscreen.keyIsPressed("escape"):
        break
    #clear Screen
    pscreen.clearScreen((0,0,0))
    #Asteroid spawn point
    aC=random.randint(1,100)
    #movement
    #move left
    if pscreen.keyIsPressed("a") or pscreen.keyIsPressed("left"):
        pX-=3
    #move right
    if pscreen.keyIsPressed("d") or pscreen.keyIsPressed("right"):
        pX+=3
    #sides of map
    if pX<=0:
        pX=0
    if pX>=789:
        pX=789
    #trigger for canon
    #draw objects
    drawS()
    drawG()
    drawP()
    
    #shoot a bullet
    if pscreen.keyIsPressed("space") and time.time()>=bullet_recharge_time:
        bullet_recharge_time = time.time()+1*0.5
        #create a bullet
        Bullet_list.append([pX+10,pY-30])
    #move Bullet
    for bullet in Bullet_list:
        bullet[1]-=1

    #draw bullet
    for bullet in Bullet_list:
        (bulletX,bulletY)=bullet
        pscreen.circle(bulletX,bulletY,5,(255,215,0),0)

    #bullets leaving the screen
    for bullet in Bullet_list:
        if bullet[1]<=0:
            Bullet_list.remove(bullet)

    #Asteroids
    #1 percent chance to spawn an asteroid
    if aC==1:
        A_list.append([random.randint(10,789),0])
    #draw Asteroid
    for Asteroid in A_list:
        (Ax,Ay)=Asteroid
        pscreen.circle(Ax,Ay,20,(112,138,144),0)
    for Asteroid in A_list:
        Asteroid[1]+=1

    #Asteroid Collisions
    #Collision with ground
    for Asteroid in A_list:
        if Asteroid[1]>=515:
            A_list.remove(Asteroid)
            pop-=random.randint(50,200)
    #Collision between Asteroid and Bullet
    for Asteroid in A_list:
        (Ax,Ay)=Asteroid
        for bullet in Bullet_list:
            (bulletX,bulletY)=bullet
            if distance(Ax,Ay,bulletX,bulletY)<25:
                A_list.remove(Asteroid)
                Bullet_list.remove(bullet)
    #Time
    sTime=time.time()-startTime
    sTime=int(sTime*10)/10
    #End game if Population is wiped out
    if pop<=0:
        break
    #display number of bullets
    pscreen.fontWrite(0,0,'Bullets:'+str(len(Bullet_list)))
    #display number of Asteroids
    pscreen.fontWrite(100,0,'Asteroids:'+str(len(A_list)))
    #display population number
    pscreen.fontWrite(0,550,'Population:'+str(pop))
    #display time
    pscreen.fontWrite(150,550,"Survival Time:"+str(sTime))
    #updateScreen
    pscreen.updateScreen()
gameOver()

#unloadScreen   
pscreen.unloadScreen()
