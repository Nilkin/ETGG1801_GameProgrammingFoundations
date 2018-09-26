#bouncing ball - OOP version - Many Instances
import pscreen
import random
import math
class Ball(object):
    def __init__(self,x=400,y=300,speed=1,angle=0,radius=20,color=(255,255,255)):
        self.x=x
        self.y=y
        self.speed=speed
        self.angle=angle
        self.radius=radius
        self.color=color
        def move(self):
            dy=-1*self.speed*math.sin(math.radians(self.angle))
            dx=self.speed*math.cos(math.radians(self.angle))
            self.y+=dy
            self.x+=dx
            #bounce off screen edges
            if self.x<0:
                dx*=-1
            if self.x>799:
                dx*=-1
            if self.y<0:
                dy*=-1
            if self.y>599:
                dy*=-1
            self.angle=math.degrees(math.atan2(-dy,dx))
        def draw(self):
            pscreen.circle(self.x,self.y,self.radius,self.color,0)
            pscreen.circle(self.x-self.radius*0.35,self.y-self.radius*0.35,self.radius*0.2,(255,255,255),0)
            pscreen.loadScreen()
#create object instances
ball_list=[]
for i in range(0,100):
    rand_speed=random.uniform(0.1,3.0)
    rand_angle=random.randint(0,359)
    rand_radius=random.randint(5,30)
    rand_color=(random.randint(50,255),random.randint(50,255),random.randint(50,255))
    ball_list.append(Ball(400,300,rand_speed,rand_angle,rand_radius,rand_color))
while True:
    if pscreen.keyIsPressed("escape"):
        break
    pscreen.clearScreen((0,0,0))
    for ball in ball_list:
        ball.move()
        ball.draw()
    pscreen.updateScreen()
pscreen.unloadScreen() 
