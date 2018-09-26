#More With Vecotrs
#18 November, 2015

#More with sin/cosine:
    #Sin(angle)-gives verticle (up/down) displacement at the angle specified.
    #Cos(angle)-gives Horizontal (left/right) displacement at the angle specified.

#Other uses:
    #1.) Drawing at angles.
    #2.) applying forces at angles.
#rotating ship example
#imports
import pscreen
import math
import random


def draw_ship(x,y,angle,thrust):
    # y is inverted in the screen, so use subtraction rather than addition.

    #draw thrust lines coming out of the back of the ship
    if thrust>0:
        for i in range(0,20):
            flame_length=random.randint(10,50)
            flame_spread=random.randint(-30,30)
            flame_x=x+flame_length*math.cos(math.radians(angle+180+flame_spread))
            flame_y=y-flame_length*math.sin(math.radians(angle+180+flame_spread))
            pscreen.line(x,y,flame_x,flame_y,(random.randint(150,255),random.randint(0,100),0),6)

    p1x=x+40*math.cos(math.radians(angle))
    p1y=y-40*math.sin(math.radians(angle))
    p2x=x+25*math.cos(math.radians(angle+120))
    p2y=y-25*math.sin(math.radians(angle+120))
    p3x=x+5*math.cos(math.radians(angle+180))
    p3y=y-5*math.sin(math.radians(angle+180))
    p4x=x+25*math.cos(math.radians(angle-120))
    p4y=y-25*math.sin(math.radians(angle-120))
    pscreen.triangle(p1x,p1y,p2x,p2y,p3x,p3y,(100,0,200),0)
    pscreen.triangle(p1x,p1y,p3x,p3y,p4x,p4y,(80,0,150),0)
    
pscreen.loadScreen()

ship_x=400
ship_y=300
ship_speed=0
ship_angle_facing=0
ship_angle_travel=0

modulation_angle=0

target_x=400
target_y=300

while True:
    if pscreen.keyIsPressed("escape"):
        break
    if pscreen.keyIsPressed("a"):
        ship_angle_facing+=1
    if pscreen.keyIsPressed("d"):
        ship_angle_facing-=1
    if pscreen.keyIsPressed("w"):
        thrust_force=0.01
    else:
        thrust_force=0
    
        

    #move ship
    dx=ship_speed*math.cos(math.radians(ship_angle_travel))
    dy=-1*ship_speed*math.sin(math.radians(ship_angle_travel))

    #apply thrust
    thrust_force_dx=thrust_force*math.cos(math.radians(ship_angle_facing))
    thrust_force_dy=thrust_force*-1*math.sin(math.radians(ship_angle_facing))

    #resultant calculation
    resultant_dx = dx + thrust_force_dx
    resultant_dy = dy + thrust_force_dy

    #convert back to get new angle and speed
    ship_speed=(resultant_dx**2 + resultant_dy**2)**0.5
    ship_angle_travel= math.degrees(math.atan2(-resultant_dy,resultant_dx))

    #update position of ship
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

    #draw everything
    #pscreen.clearScreen((0,0,0,5))
    pscreen.rectangle(0,0,799,599,(0,0,0,5),0) #leave motion blur by clearing with alpha

    modulation_angle+=1
    #draw planet
    pscreen.circle(400,300,100+10*math.sin(math.radians(modulation_angle/2)),(150+50*math.sin(math.radians(modulation_angle)),150+50*math.sin(math.radians(modulation_angle+120)),150+50*math.sin(math.radians(modulation_angle+240))),0)
    #draw target
    pscreen.circle(target_x+100*math.sin(math.radians(modulation_angle*2)),target_y+200*math.sin(math.radians(modulation_angle*1.5)),10,(255,255,255),0)
    
    
    draw_ship(ship_x,ship_y,ship_angle_facing,thrust_force)
    pscreen.updateScreen()

pscreen.unloadScreen()

