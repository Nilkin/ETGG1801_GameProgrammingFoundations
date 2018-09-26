#More With Vecotrs
#18 November, 2015

#More with sin/cosine:
    #Sin(angle)-gives verticle (up/down) displacement at the angle specified.
    #Cos(angle)-gives Horizontal (left/right) displacement at the angle specified.

#Other uses:
    #1.) Drawing at angles.
    #2.) applying forces at angles.
#Rotating ship example
#imports
import math
import pscreen
import random

#load screen
pscreen.loadScreen()    
#rotating ship
#y is inverted on the screen so uses subtraction rather than addition
def draw_Ship(x,y,angle,thrust):
    #draws thrust lines coming from back of the ship
    if thrust>0:
        for i in range(0,10):
            flame_length=random.randint(25,40)
            flame_spread=random.randint(-30,30)
            flame_x=x+flame_length*math.cos(math.radians(angle+180+flame_spread))
            flame_y=y-flame_length*math.sin(math.radians(angle+180+flame_spread))
            pscreen.line(x,y,flame_x,flame_y,(random.randint(100,200),random.randint(50,150),random.randint(100,175)),4)
    #draws ship
    p1x=x+40*math.cos(math.radians(angle))
    p1y=y-40*math.sin(math.radians(angle))
    p2x=x+25*math.cos(math.radians(angle+120))
    p2y=y-25*math.sin(math.radians(angle+120))
    p3x=x+10*math.cos(math.radians(angle+180))
    p3y=y-10*math.sin(math.radians(angle+180))
    p4x=x+25*math.cos(math.radians(angle-120))
    p4y=y-25*math.sin(math.radians(angle-120))
    pscreen.triangle(p1x,p1y,p2x,p2y,p3x,p3y,(200,0,255),0)
    pscreen.triangle(p1x,p1y,p3x,p3y,p4x,p4y,(255,0,200),0)
ship_x=400
ship_y=300
ship_speed=0
ship_angle_facing=0
ship_angle_travel=0

modulation_angle=0

target_x=400
target_y=300

#Game loop
while True:
    if pscreen.keyIsPressed("escape"):
        break
    if pscreen.keyIsPressed('a'):
        ship_angle_facing+=1
    if pscreen.keyIsPressed('d'):
        ship_angle_facing-=1
    if pscreen.keyIsPressed('w'):
        thrust_force=0.1
    else:
        thrust_force=0
    

    #limit speed
    if ship_speed>=20:
        ship_speed=20
    if ship_speed<=0:
        ship_speed=0
    #Move ship
    dx=ship_speed*math.cos(math.radians(ship_angle_travel))
    dy=-1*ship_speed*math.sin(math.radians(ship_angle_travel))

    #apply Thrust
    thrust_force_dx=thrust_force*math.cos(math.radians(ship_angle_facing))
    thrust_force_dy=thrust_force*-1*math.sin(math.radians(ship_angle_facing))

    #resultant calculation
    resultant_dx= dx+thrust_force_dx
    resultant_dy= dy+thrust_force_dy

    #convert back to get new angle and speed
    ship_speed= (resultant_dx**2 +resultant_dy**2)**0.5
    ship_angle_travel=math.degrees(math.atan2(-resultant_dy,resultant_dx))
    
    ship_x+=resultant_dx
    ship_y+=resultant_dy

    #wrap ship on screen
    if ship_x<0:
        ship_x=799
    if ship_x>799:
        ship_x=0
    if ship_y<0:
        ship_y=599
    if ship_y>599:
        ship_y=0

    #clear screen
    pscreen.clearScreen((0,0,0))
    #draw target
    pscreen.circle(target_x+100*math.sin(math.radians(modulation_angle)),target_y,10,(255,255,255),0)
    #draw pulsating planet
    pscreen.circle(400,300,100+10*math.sin(math.radians(modulation_angle)),150,240+50*math.sin(math.radians(math.radians(modulation_angle)),0),0)
    modulation_angle+=1
    #draw ship
    draw_Ship(ship_x,ship_y,ship_angle_facing,thrust_force)
    #UpdateScreen
    pscreen.updateScreen()

#unloadScreen
pscreen.unloadScreen()

    #3.)Modulating game parameters:
        #*Size
        #*Color
        #*Position
        #*Speed
        #*Angle
        #*Pretty much anything
