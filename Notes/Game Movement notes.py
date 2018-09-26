# continuous movement example
import pscreen
pscreen.loadScreen()
playerX=100
playerY=100
playerDx=1
playerDy=0
playerInitialSpeed=2
frictionFactor=0.999
enemyX=300
enemyY=300
enemyDx=1
enemyDy=1
enemyInitialSpeed=1
enemy2X=400
enemy2Y=500
enemy2Dx=0.8
enemy2Dy=0.8
enemy2InitialSpeed=0.8
while True:
    #user input
    if pscreen.keyIsPressed("escape"):
        break
    if pscreen.keyIsPressed("a"):
        playerDx=-playerInitialSpeed
        playerDy=0
    if pscreen.keyIsPressed("d"):
        playerDx=playerInitialSpeed
        playerDy=0
    if pscreen.keyIsPressed("w"):
        playerDy=-playerInitialSpeed
        playerDx=0
    if pscreen.keyIsPressed("s"):
        playerDy=playerInitialSpeed
        playerDx=0
        #apply friction
        playerDx*=frictionFactor
        playerDy*=frictionFactor
        #update position
        playerX+=playerDx
        playerY+=playerDy
        #check for border of screen
    if playerX<=0 or playerX>=799:
        playerDx*=-1
    if playerY<=0 or playerY>=599:
        playerDy*=-1
    #bound player on screen
    if playerX<0:
        playerX=0
    if playerX>799:
        playerX=799
    if playerY<0:
        playerY=0
    if playerY>599:
        playerY=599
    #update enemy position
    enemyX+=enemyDx
    enemyY+=enemyDy
    #check for border of screen
    if enemyX<=0 or enemyX>=799:
        enemyDx*=-1
    if enemyY<=0 or enemyY>=599:
        enemyDy*=-1
    #bound player on screen
    if enemyX<0:
        enemyX=0
    if enemyX>799:
        enemyX=799
    if enemyY<0:
        enemyY=0
    if enemyY>599:
        enemyY=599
    #update enemy2 position
    enemy2X+=enemy2Dx
    enemy2Y+=enemy2Dy
    #check for border of screen
    if enemy2X<=0 or enemy2X>=799:
        enemy2Dx*=-1
    if enemy2Y<=0 or enemy2Y>=599:
        enemy2Dy*=-1
    #bound player on screen
    if enemy2X<0:
        enemy2X=0
    if enemy2X>799:
        enemy2X=799
    if enemy2Y<0:
        enemy2Y=0
    if enemy2Y>599:
        enemy2Y=599
    #render screen
    pscreen.clearScreen((0,0,0))
    #draw player
    pscreen.circle(int(playerX),int(playerY),20,(0,255,0),0)
    #draw enemy
    pscreen.circle(int(enemyX),int(enemyY),20,(255,0,0),0)
    #draw enemy2
    pscreen.circle(int(enemy2X),int(enemy2Y),20,(255,0,0),0)
    pscreen.updateScreen()
pscreen.unloadScreen()
