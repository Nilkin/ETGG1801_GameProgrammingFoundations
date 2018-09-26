#More Object Oriented Programming
#11/30/15

#attributes-data associated with an object.} Properties or Object Variables
#Abilities- functionality associated with an object.} Methods or Object functions
#In Python, we must first define a class.
#A class is like a blueprint for a specific type of object.
#A class defines the properties and methods that an object will have when it is created.

#__init__ is the "Constructor", a special object function that gets executed at time an object is created with this class.
#The code in the constructor is usually used to create the variables and add them to the created object instance.
#def move(self):
    #Code to move the object based upon the speed/direction/position of the object itself.
#def draw(self)
    #Code to draw the object on the screen based upon the position, color, radius, etc of the object itself.
#Every object function has self as the first ting in the parameter.
    #This gives every fuction the ability to modify parts of itself.

#Lists are a sequence of anything
#Draw Star example
import pscreen
import math
import random
class Pentagram(object):
    def __init__(self,x=400,y=300,angle=0,color=(255,255,255),radius=40,rotation_speed=0):
        self.x=x
        self.y=y
        self.angle=angle
        self.color=color
        self.radius=radius
        self.rotation_speed=rotation_speed
    def update(self):
        self.angle+=self.rotation_speed
    def draw(self):
        self.update()
        p1x=self.x+self.radius*math.cos(math.radians(self.angle+18))
        p1y=self.y+(-1)*self.radius*math.sin(math.radians(self.angle+18))
        p2x=self.x+self.radius*math.cos(math.radians(self.angle+90))
        p2y=self.y-self.radius*math.sin(math.radians(self.angle+90))
        p3x=self.x+self.radius*math.cos(math.radians(self.angle+162))
        p3y=self.y-self.radius*math.sin(math.radians(self.angle+162))
        p4x=self.x+self.radius*math.cos(math.radians(self.angle+234))
        p4y=self.y-self.radius*math.sin(math.radians(self.angle+234))
        p5x=self.x+self.radius*math.cos(math.radians(self.angle+308))
        p5y=self.y-self.radius*math.sin(math.radians(self.angle+308))
        pscreen.line(p1x,p1y,p3x,p3y,self.color,1)
        pscreen.line(p1x,p1y,p4x,p4y,self.color,1)
        pscreen.line(p2x,p2y,p4x,p4y,self.color,1)
        pscreen.line(p2x,p2y,p5x,p5y,self.color,1)
        pscreen.line(p3x,p3y,p5x,p5y,self.color,1)
        pscreen.circle(self.x,self.y,self.radius,self.color,1)
        
pscreen.loadScreen()
pentagram_list=[]

for i in range(0,10):
    pentagram_list.append(Pentagram(x=random.randint(0,799),y=random.randint(0,599),radius=random.randint(10,50),rotation_speed=random.uniform(-1,1)))

while True:
    if pscreen.keyIsPressed("escape"):
        break
    pscreen.clearScreen((0,0,0))
    for p_gram in pentagram_list:
        p_gram.draw()

    pscreen.updateScreen()

pscreen.unloadScreen
