Method 1: identical Position check
    #check for collision
    if PlayerX == TreasureX and PlayerY == TreasureY:
        They are colliding! do something!
    else:
        They are not.
Problem!: doesnt account for radius.
    unnatural
    furstrating to player
    positions have to match exactlty

Method 2: Bounding box
    #check for collision
    if abs(TreasureX-PlayerX)<=(PlayerR+TreasureR) and abs(TreasureY-PlayerY)<=(PlayerR+TreasureR):
        Colliding! Do Something!
    else:
        They are not!

Distance Calculation
    use pythagorean therom.

Method 3: Distance check
    #check for collision
distance= ((TreasureX-PlayerX)**2+(TreasureY-PlayerY)**2))**0.5
if distance <= PlayerR+TreasureR:
    Colliding! Do something!
else:
    Not Colliding

#Demonstration of collision methods
#Collsion Detection Example:

#imports
import pscreen

#player position
px=100
py=100
#player radius
pr=20
#treasure position
tx=400
ty=400
#treasure radius
tr=20

#initialization
pscreen.loadScreen()

#game loop
while True:
    pscreen.clearScreen()
    if pscreen.keyIsPressed("escape"):
        break
    if pscreen.keyIsPressed("a"):
        px-=1
    if pscreen.keyIsPressed("d"):
        px+=1
    if pscreen.keyIsPressed("w"):
        py-=1
    if pscreen.keyIsPressed("s"):
        py+=1
    #player
    pscreen.circle(px,py,pr,(0,255,0),0)
    #treasure
    pscreen.circle(tx,ty,tr,(255,255,0),0)

    #Check for collision
    #method 1:same location
    #if px==tx and py==ty:
       # pscreen.line(0,0,799,599,(255,0,0),10)
       # pscreen.line(0,599,799,0,(255,0,0),10)

    #method 2:bounding box overlap
    #if abs(tx-px)<=tr+pr and abs(ty-py)<=tr+pr:
        # pscreen.line(0,0,799,599,(255,0,0),10)
        # pscreen.line(0,599,799,0,(255,0,0),10)

    #method 3: distance check
    #distance = ((tx-px)**2 + (ty-py)**2))**0.5
    #if distance <= tr+pr:
        # pscreen.line(0,0,799,599,(255,0,0),10)
        # pscreen.line(0,599,799,0,(255,0,0),10)
    pscreen.updateScreen()

#unload process
pscreen.unloadScreen()

#import time
#time.time()
#startTime=time.time
#60-(time.time()-startTime)
    
