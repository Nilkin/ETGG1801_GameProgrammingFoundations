#Object Oriented example 1


import pscreen
import random
import time
import math

class Ball(object):
    def __init__ (self,x=400,y=300,speed=1,direction=0,radius=20,color=(255,255,255,0)):
        self.x=x
        self.y=y
        self.speed=speed
        self.direction=direction
        self.radius=radius
        self.color=color
    def move(self):
        dy=-1*self.speed*math.sin(math.radians(self.direction))
        dx=self.speed*math.cos(math.radians(self.direction))
        self.y+=dy
        self.x+=dx
        if self.x<0:
            dx*=-1
        if self.x>799:
            dx*=-1
        if self.y<0:
            dy*=-1
        if self.y>599:
            dy*=-1
        self.direction=math.degrees(math.atan2(-dy,dx))
    def draw(self):
        pscreen.circle(self.x,self.y,self.radius,self.color,0)


pscreen.loadScreen()

#make a ball instance from the class
ball_list=[]
for i in range(0,100):
    rand_speed=random.uniform(0.1,2.0)
    rand_direction=random.randint(0,359)
    rand_radius=random.randint(10,40)
    rand_color=(random.randint(25,255),random.randint(25,255),random.randint(25,255),random.randint(25,255))
    ball_list.append(Ball(400,300,rand_speed,rand_direction,rand_radius,rand_color))

while True:
    if pscreen.keyIsPressed('escape'):
        break
    #Clear Screen
    pscreen.clearScreen((0,0,0,0))
    #Move balls and draw them in list
    for ball in ball_list:
                     ball.move()
                     ball.draw()
    
    pscreen.updateScreen()

pscreen.unloadScreen()
