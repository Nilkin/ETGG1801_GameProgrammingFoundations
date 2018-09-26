#Mathmatics/ Object oriented programming, and pscreen/pygame Notes
#Thomas Gilman
#Mr. Paul Yost
#Etgg 1801-03
#16th November, 2015

#Up to now, we have been representing motion in a simple way:
#X+=1, Y-=1, to move up and to the right, or X+=dX, Y-=dY

#We want to Represent motion more naturally:
# *direction of Motion
# *speed

#Vector Motion:
# *Directional movement where the length of the arrow is the speed
# *Natural/Realistic Movement
# *apply forces (gravity, explosions, prepulsions,etc..)
# *Move in any direction at any speed.

#To do this, we want to store the motion of a game object as:
# *Speed (distance move over some time)- an offset from the previous position.
# *Direction (angle that we are moving, heading) - used to compute change in X and Y.
#To represent an object in the game, we need to track the following things:
# *X cordinate - Objects X
# *Y cordinate - Objects Y
# *Angle - direction of travel (heading)
# *Speed - how fast it is traveling (velocity)

#How do we compute dX, dY, given angle and speed?
#dY is the up/down component (sine)
#dX is the left/right component (cosine)

#In Programming (and really in math)
#degrees are not the natural way to measure angles.
#The natural way to represent angles is in Radians.
#Why Radians?
# What Is Pi?
# radions are counted in pi, from the start of the circle being 0
#going all the way around the circle equals 2pi
# half the circle is pi
#quarter of the circle is pi/2
#half a quarter is pi/4

#So, compute dX, dY given angle and speed:
#(dY = Sin(angle)*speed) gives the up/down component with radius of 1, multipling by speed scales the speed.
#(dX = Cos(angle)*speed) same as the Y only moves left to right.

#How can we take a dX and dY and compute the angle & speed?
# pythagorean theorom (speed=(dX**2+dY**2)**.5

#tan(angle)=dY/dX
#atan(tan(angle))=atan(dY/dX)
#angle=atan(dY/dX)

#built in function:
#angle=atan2(-dY,dX)

#gravity:
#resultant_dX=dX+dX_force
#resultant_dY=dY+dY_force

#Vector Motion

import pscreen
import math

pscreen.loadScreen()

ballX=100
ballY=100
ballSpeed=1
ballAngle=45
ballJump=False

gravityForce=1

#Game Loop
while True:
    if pscreen.keyIsPressed("escape"):
        break
    if pscreen.keyIsPressed("a"):
        ballAngle+=1
    if pscreen.keyIsPressed("d"):
        ballAngle-=1
    if pscreen.keyIsPressed("w"):
        ballSpeed+=.1
    if pscreen.keyIsPressed("s"):
        ballSpeed-=.1
        if ballSpeed<0:
            ballSpeed=0
    if pscreen.keyIsPressed("space"):
        ballJump=True
    else:
        ballJump=False

    #Move ball
    dY=-1*math.sin(math.radians(ballAngle))*ballSpeed
    dX=math.cos(math.radians(ballAngle))*ballSpeed
    ballY+=dY
    ballX+=dX

    #wrap around the screen
    if ballX<0:
        dX*=-1
        dX*=.9
        dY*=.9
        ballX=0
    if ballX>799:
        dX*=-1
        dX*=.9
        dY*=.9
        ballX=799
    if ballY<0:
        dY*=-1
        dX*=.9
        dY*=.9
        ballY=0
    if ballY>599:
        dY*=-1
        dX*=.9
        dY*=.9
        ballY=599

    #add a little bit of gravity
    dY+=.1
    #add jump force
    if ballJump==True:
        dY-=5
        ballJump=False

    #convert back to possible new angle and speed
    ballSpeed=(dX**2+dY**2)**.5
    ballAngle=math.degrees(math.atan2(-dY,dX))
    #add friction
    #ballSpeed*=.9999999999999999
    #speed limit
    if ballSpeed>20:
        ballSpeed=20
    

    #draw Screen
    pscreen.clearScreen((0,0,0))
    #draw ball
    pscreen.circle(int(ballX),int(ballY),20,(255,255,0),0)
    
    #render Screen
    pscreen.updateScreen()

pscreen.unloadScreen()

