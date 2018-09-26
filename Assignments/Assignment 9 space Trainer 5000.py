#Assignment 9 "Space Trainer 5000"
#Thomas Gilman
#Paul Yost
#Etgg 1801-02
#30th November, 2015

import pscreen
import math
import time
import random

#Clears Screen to black
def clearScreen():
    pscreen.clearScreen((0,0,0))

#Modulation for pulsating stars
modulation_angle=0

#Draw Star Field
class Star(object):
    def __init__ (self,x=random.randint(10,789),y=random.randint(10,589),angle=0,radius=random.randint(4,8),color=(random.randint(5,255),random.randint(5,255),random.randint(5,255)),rotation_speed=0):
        self.x=x
        self.y=y
        self.angle=angle
        self.radius=radius
        self.color=color
        self.rotation_speed=rotation_speed
    def update(self):
        self.angle+=self.rotation_speed
    def drawStar(self):
        self.update()
        self.radius+=.02*math.sin(math.radians(modulation_angle))
        p1x=self.x+self.radius*math.cos(math.radians(self.angle+18))
        p1y=self.y+(-1)*self.radius*math.sin(math.radians(self.angle+18))
        p2x=self.x+self.radius*math.cos(math.radians(self.angle+90))
        p2y=self.y+(-1)*self.radius*math.sin(math.radians(self.angle+90))
        p3x=self.x+self.radius*math.cos(math.radians(self.angle+162))
        p3y=self.y+(-1)*self.radius*math.sin(math.radians(self.angle+162))
        p4x=self.x+self.radius*math.cos(math.radians(self.angle+238))
        p4y=self.y+(-1)*self.radius*math.sin(math.radians(self.angle+238))
        p5x=self.x+self.radius*math.cos(math.radians(self.angle+308))
        p5y=self.y+(-1)*self.radius*math.sin(math.radians(self.angle+308))
        pscreen.line(p1x,p1y,p3x,p3y,self.color,1)
        pscreen.line(p1x,p1y,p4x,p4y,self.color,1)
        pscreen.line(p2x,p2y,p4x,p4y,self.color,1)
        pscreen.line(p2x,p2y,p5x,p5y,self.color,1)
        pscreen.line(p3x,p3y,p5x,p5y,self.color,1)

#ship def
def draw_ship(x,y,angle,thrust):
    #ship
    p1x=x+25*math.cos(math.radians(angle))
    p1y=y-25*math.sin(math.radians(angle))
    p2x=x+15*math.cos(math.radians(angle+110))
    p2y=y-15*math.sin(math.radians(angle+110))
    p3x=x+2*math.cos(math.radians(angle+180))
    p3y=y-2*math.sin(math.radians(angle+180))
    p4x=x+15*math.cos(math.radians(angle-110))
    p4y=y-15*math.sin(math.radians(angle-110))
    pscreen.triangle(p1x,p1y,p2x,p2y,p3x,p3y,(150,25,168),0)
    pscreen.triangle(p1x,p1y,p3x,p3y,p4x,p4y,(150,25,168),0)
#ship2 def
def draw_ship2(x2,y2,angle2,thurst2):
    #second player ship
    p21x=x2+25*math.cos(math.radians(angle2))
    p21y=y2-25*math.sin(math.radians(angle2))
    p22x=x2+15*math.cos(math.radians(angle2+110))
    p22y=y2-15*math.sin(math.radians(angle2+110))
    p23x=x2+2*math.cos(math.radians(angle2+180))
    p23y=y2-2*math.sin(math.radians(angle2+180))
    p24x=x2+15*math.cos(math.radians(angle2-110))
    p24y=y2-15*math.sin(math.radians(angle2-110))
    pscreen.triangle(p21x,p21y,p22x,p22y,p23x,p23y,(168,255,150),0)
    pscreen.triangle(p21x,p21y,p23x,p23y,p24x,p24y,(168,255,150),0)

#item def
def draw_target(x,y,radius,color):
    tx=random.randint(10,789)
    ty=random.randint(10,589)
    tradius=100
    tcolor=(168,178,100)
    pscreen.circle(x,y,tradius,color,0)

#distance def
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

#Time def
def gameTime():
    timeLeft=endTime-time.time()
    timeLeft=int(timeLeft*10)/10
    pscreen.fontSelect("Arial",18)
    pscreen.fontWrite(700,5,"Time Left:"+str(timeLeft))

#game over def
def gameOver():
    pscreen.fontSelect("Arial",22)
    pscreen.fontWrite(350,300,"Game Over")
    pscreen.fontWrite(250,325,"Player1 Score:"+str(score))
    pscreen.fontWrite(410,325,"Player2 Score:"+str(score2))
    if score>score2:
        pscreen.fontWrite(360,375,"Player1 Wins!")
    elif score<score2:
        pscreen.fontWrite(360,375,"Player2 Wins!")
    elif score==score2:
        pscreen.fontWrite(360,375,"Tie!")

#floating meteor obsticle
def meteor():
    #meteor object
    pscreen.circle(mX,mY,mR,(30,26,18),0)
    
#load screen
pscreen.loadScreen()
#load font
pscreen.fontSelect('Arial',16)
#load Time
startTime=time.time()
endTime=startTime+60
#star list
star_list=[]
#render stars
for i in range(0,12):
    star_list.append(Star(x=random.randint(10,789),y=random.randint(0,589),rotation_speed=random.uniform(-1,1)))
#Meteor specs
mX=random.randint(10,789)#x cord
mY=random.randint(10,589)#y cord
mR=25#radius
mDx=1
mDy=1
mSpeed=1#speed of meteor
mIspeed=1#initial speed
#ship specs
ship_x=400
ship_y=300
ship_speed=0
ship_angle_facing=0
ship_angle_travel=0
#second player ship specs
ship2_x=200
ship2_y=500
ship2_speed=0
ship2_angle_facing=0
ship2_angle_travel=0
#item specs
tx=700
ty=500
tradius=100
tcolor=(168,178,100)
#score
score=0
#second player score
score2=0

#Game Loop
while True:
    if pscreen.keyIsPressed("escape"):
        break
    #ship rotation and force
    if pscreen.keyIsPressed("a"):
        ship_angle_facing+=1
    if pscreen.keyIsPressed("d"):
        ship_angle_facing-=1
    if pscreen.keyIsPressed("w"):
        thrust_force=0.01
    elif pscreen.keyIsPressed("s"):
        thrust_force=-0.01
    else:
        thrust_force=0
    #second player ship rotation and force
    if pscreen.keyIsPressed("j"):
        ship2_angle_facing+=1
    if pscreen.keyIsPressed("l"):
        ship2_angle_facing-=1
    if pscreen.keyIsPressed("i"):
        thrust2_force=0.01
    elif pscreen.keyIsPressed("k"):
        thrust2_force=-0.01
    else:
        thrust2_force=0
    #clear Screen
    clearScreen()
    #draw stars
    for s_ar in star_list:
        s_ar.drawStar()
    #pulsate Stars
    modulation_angle+=1
    #movement of Ship1
    dx=ship_speed*math.cos(math.radians(ship_angle_travel))
    dy=-1*ship_speed*math.sin(math.radians(ship_angle_travel))
    #thrust application1
    thrust_force_dx=thrust_force*math.cos(math.radians(ship_angle_facing))
    thrust_force_dy=thrust_force*-1*math.sin(math.radians(ship_angle_facing))
    #result1
    end_dx=dx+thrust_force_dx
    end_dy=dy+thrust_force_dy
    #swap from radians and new speed1
    ship_speed=(end_dx**2+end_dy**2)**0.5
    ship_angle_travel=math.degrees(math.atan2(-end_dy,end_dx))
    #render ships position1
    ship_x+=end_dx
    ship_y+=end_dy
    #wrap the screen for ship 1
    if ship_x<0:
        ship_x=799
    if ship_x>799:
        ship_x=0
    if ship_y<0:
        ship_y=599
    if ship_y>599:
        ship_y=0
    #limiters for ship 1
    if thrust_force>1:
        thrust_force=1
    if thrust_force<-1:
        thrust_force=-1
    if ship_speed>5:
        ship_speed=5
    if ship_speed<-5:
        ship_speed=-5
    #movement of Ship2
    d2x=ship2_speed*math.cos(math.radians(ship2_angle_travel))
    d2y=-1*ship2_speed*math.sin(math.radians(ship2_angle_travel))
    #thrust application2
    thrust_force_d2x=thrust2_force*math.cos(math.radians(ship2_angle_facing))
    thrust_force_d2y=thrust2_force*-1*math.sin(math.radians(ship2_angle_facing))
    #result2
    end_d2x=d2x+thrust_force_d2x
    end_d2y=d2y+thrust_force_d2y
    #swap from radians and new speed2
    ship2_speed=(end_d2x**2+end_d2y**2)**0.5
    ship2_angle_travel=math.degrees(math.atan2(-end_d2y,end_d2x))
    #render ships position2
    ship2_x+=end_d2x
    ship2_y+=end_d2y
    #wrap the screen for ship 2
    if ship2_x<0:
        ship2_x=799
    if ship2_x>799:
        ship2_x=0
    if ship2_y<0:
        ship2_y=599
    if ship2_y>599:
        ship2_y=0
    #limiters for ship 2
    if thrust2_force>1:
        thrust2_force=1
    if thrust2_force<-1:
        thrust2_force=-1
    if ship2_speed>5:
        ship2_speed=5
    if ship2_speed<-5:
        ship2_speed=-5
    #Meteor warping on screen
    if mX<=0 or mX>=799:
        mDx*=-1
    if mY<0 or mY>=599:
        mDy*=-1
    #Meteor update position
    mX+=mDx
    mY+=mDy
    #distance between ship 1 and target
    if distance(ship_x,ship_y,tx,ty)<125:
        tx=random.randint(10,789)
        ty=random.randint(10,589)
        score+=10
    #distance between ship 2 and target
    if distance(ship2_x,ship2_y,tx,ty)<125:
        tx=random.randint(10,789)
        ty=random.randint(10,589)
        score2+=10
    #distance between ship 1 and meteor
    if distance(ship_x,ship_y,mX,mY)<50:
        mDx*=-1
        mDy*=-1
        ship_speed*=-1
        score*=0
    #distance between ship 2 and meteor
    if distance(ship2_x,ship2_y,mX,mY)<50:
        mDx*=-1
        mDy*=-1
        ship2_speed*=-1
        score2*=0
    #end game
    timeLeft=endTime-time.time()
    if timeLeft<=0:
        break
    #draw Target
    draw_target(tx,ty,tradius,tcolor)
    #draw Meteor
    meteor()
    #draw player 1
    draw_ship(ship_x,ship_y,ship_angle_facing,thrust_force)
    #draw player 2
    draw_ship2(ship2_x,ship2_y,ship2_angle_facing,thrust2_force)
    #show Score
    pscreen.fontWrite(0,0,"Player1 Score"+str(score))
    pscreen.fontWrite(150,0,"Player2 Score:"+str(score2))
    #show Time
    gameTime()
    #update Screen in loop
    pscreen.updateScreen()
gameOver()
pscreen.updateScreen()
time.sleep(5)
#Unload Screen
pscreen.unloadScreen()
