#Time Function Notes

#imports
import pscreen
import time
#time functions:
#time.sleep(5)
#time.time()#returns a number of seconds since the "Epoch" January 1 1970 GMT
#The idea is to make an event that is timed:
    #capture current time -> start time
    #calculate current time of future event.(add a number to the captured time)
    #wait for new current time to exceed calculated event time.
    #if the event time has been reached, take action.
#Ex: Delay for a number of seconds:
#startTime=time.time()
#eventTime=startTime+5
#while True:
    #if time.time()>=eventTime:
        #break
#print("done!")

#Movement Notes
#move right (px+=1) increasing x
#move left (px-=1) decreasing x
#move up (py-=1) decreasing y
#move down (py+=1) increasing y
#change it to dx and dy and make it equal to 1 to constantly increase
#or make it equal to -1  to constantly decrease.

#continuos movement example

#load screen
pscreen.loadScreen()

playerX=100
playerY=100
playerDx=0
playerDy=0
playerSpeed=1
playerInitialSpeed=2
frictionFactor=0.999

enemyX=300
enemyY=300
enemyDx=1
enemyDy=1
enemyInitialSpeed=1

#gameLoop

while True:
    
    #escape user input
    if pscreen.keyIsPressed("escape"):
        break
    if pscreen.keyIsPressed("a"):
        playerDx=-playerInitialSpeed
        playerDx=-1
    if pscreen.keyIsPressed("d"):
        playerDx=playerInitialSpeed
        playerDx=1
    if pscreen.keyIsPressed("w"):
        playerDy=-playerInitialSpeed
        playerDy=-1
    if pscreen.keyIsPressed("s"):
        playerDy=playerInitialSpeed
        playerDy=1
    #apply Friction
    playerDx*=frictionFactor
    playerDy*=frictionFactor
    #update position
    playerX+=playerDx
    playerY+=playerDy
    enemyX+=enemyDx
    enemyY+=enemyDy
    #bound player on screen
    if playerX<=0 or playerX>=799:
        playerDx*=-1
    if playerY<=0 or playerY>=599:
        playerDy*=-1
    if playerX<0:
        playerX=0
    if playerX>799:
        playerX=799
    if playerY<0:
        playerY=0
    if playerY>599:
        playerY=599
   #bound enemy on screen
    if enemyX<=0 or enemyX>=799:
        enemyDx*=-1
    if enemyY<=0 or enemyY>=599:
        enemyDy*=-1
    if enemyX<0:
        enemyX=0
    if enemyX>799:
        enemyX=799
    if enemyY<0:
        enemyY=0
    if enemyY>599:
        enemyY=599
    #renderScreen
    pscreen.clearScreen((0,0,0))

    #drawPlayer
    pscreen.circle(int(playerX),int(playerY),20,(255,255,0),0)
    
    
    #refresh screen
    pscreen.updateScreen()


#unloadScreen
pscreen.unloadScreen()
