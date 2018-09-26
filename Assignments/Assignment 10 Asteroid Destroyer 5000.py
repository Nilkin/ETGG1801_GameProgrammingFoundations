#Assignment 10: Asteroid Destroyer 5000
#Thomas Gilman
#Paul Yost
#ETGG 1801-02
#6th December, 2015

#imports
import pscreen
import random
import time
import math

#time
startTime=time.time()
#font

#classes
#Asteroid class
class Asteroid(object):
    def __init__(self,x=random.randint(10,789),y=random.randint(10,589),heading=0,speed=1,angle=random.randint(0,360),radius=35, color=(105,105,105),rotation_speed=0):
        self.x=x
        self.y=y
        self.heading=heading
        self.speed=speed
        self.angle=angle
        self.radius=radius
        self.color=color
        self.rotation_speed=rotation_speed
    def update(self):
        #movement of Asteroid
        dx=self.speed*math.cos(math.radians(self.angle))
        dy=self.speed*(-1)*math.sin(math.radians(self.angle))
        self.heading=math.degrees(math.atan2(-dy,dx))
        self.speed=(dx**2+dy**2)**0.5
        self.x+=dx
        self.y+=dy
        if self.x>799:
            self.x=0
        if self.x<0:
            self.x=799
        if self.y>599:
            self.y=0
        if self.y<0:
            self.y=599
    def render(self):
        self.update()
        p1x=self.x+self.radius*math.cos(math.radians(self.angle))
        p1y=self.y+(-1)*self.radius*math.sin(math.radians(self.angle))
        p2x=(self.x-5)+self.radius*math.cos(math.radians(self.angle))
        p2y=(self.y-5)+(-1)*self.radius*math.sin(math.radians(self.angle))
        #print(p1x,p1y)
        pscreen.circle(p1x,p1y,self.radius,self.color,0)
        pscreen.circle(p2x,p2y,5,(0,0,0),0)

#Ship
#ship global setting
class Ship(object):
    def __init__(self,x=400,y=300,angle=0,heading=0,speed=0,thrust=False,shield=False,energy=100):
        self.x=x
        self.y=y
        self.angle=angle
        self.heading=heading
        self.speed=speed
        self.thrust=thrust
        self.shield=shield
        self.thrust_force=0
        self.energy=energy
    #Thrust
    def thrust(self):
        #call rotation
        Ship.rotate_cw(self)
        Ship.rotate_ccw(self)
        #apply Thrust
        thrust_force_dx=self.thrust_force*math.cos(math.radians(self.angle))
        thrust_force_dy=(-1)*self.thrust_force*math.sin(math.radians(self.angle))
        #move ship
        dx=self.speed*math.cos(math.radians(self.heading))
        dy=self.speed*(-1)*math.sin(math.radians(self.heading))
        #Result dx, and dy
        result_dx=dx+thrust_force_dx
        result_dy=dy+thrust_force_dy
        #new x and y
        self.x+=result_dx
        self.y+=result_dy
        #update speed
        self.speed=(result_dx**2+result_dy**2)**0.5
        #update angle travel
        self.heading=math.degrees(math.atan2(-result_dy,result_dx))
    #Rotate ship clockwise
    def rotate_cw(self):
        if pscreen.keyIsPressed('d'):
            self.angle-=5
    #Rotate ship counter clockwise
    def rotate_ccw(self):
        if pscreen.keyIsPressed('a'):
            self.angle+=5
    #Render the Ship
    def draw_Ship(self):
        Ship.move(self)
        if self.shield==True:
            pscreen.circle(self.x,self.y,25,(132,112,255),1)
        p1x=self.x+25*math.cos(math.radians(self.angle))
        p1y=self.y-25*math.sin(math.radians(self.angle))
        p2x=self.x+15*math.cos(math.radians(self.angle+120))
        p2y=self.y-15*math.sin(math.radians(self.angle+120))
        p3x=self.x+5*math.cos(math.radians(self.angle+180))
        p3y=self.y-5*math.sin(math.radians(self.angle+180))
        p4x=self.x+15*math.cos(math.radians(self.angle-120))
        p4y=self.y-15*math.sin(math.radians(self.angle-120))
        pscreen.triangle(p1x,p1y,p2x,p2y,p3x,p3y,(72,61,139),0)
        pscreen.triangle(p1x,p1y,p3x,p3y,p4x,p4y,(0,191,255),0)
        #draw flame behind ship when thrusting
        if self.thrust==True:
            for i in range(0,5):
                flame_length=random.randint(25,40)
                flame_spread=random.randint(-15,15)
                flame_x=self.x+flame_length*math.cos(math.radians(self.angle+180+flame_spread))
                flame_y=self.y-flame_length*math.sin(math.radians(self.angle+180+flame_spread))
                pscreen.line(self.x,self.y,flame_x,flame_y,(random.randint(150,200),random.randint(100,150),random.randint(150,175)),4)
    #Move the ship
    def move(self):
        Ship.thrust(self)
        #Move ship forward in space
        if pscreen.keyIsPressed("w"):
            self.thrust_force+=.0001
            self.thrust=True
        else:
            self.thrust_force=0
            self.thrust=False
        #wrap ship on screen
        if self.x<0:
            self.x=799
        if self.x>799:
            self.x=0
        if self.y<0:
            self.y=599
        if self.y>599:
            self.y=0
        #limit speed
        if self.speed>=15:
            self.speed=15
        if self.speed<=0:
            self.speed=0

#Bullet
class Bullet(object):
    def __init__(self,x,y,heading,speed=.01,size=5,lifeleft=100):
        self.x=ship.x
        self.y=ship.y
        self.heading=ship.angle
        self.speed=speed
        self.size=size
        self.lifeleft=lifeleft
    def render(self):
        pscreen.circle(self.x,self.y,self.size,(255,135,0),0)
    def move(self):
        #move the bullet
        dx=self.speed*math.cos(math.radians(self.heading))
        dy=self.speed*(-1)*math.sin(math.radians(self.heading))
        result_dx=dx
        result_dy=dy
        #update location
        self.x+=result_dx
        self.y+=result_dy
        #wrap on screen
        if self.x>799:
            self.x=0
        if self.x<0:
            self.x=799
        if self.y>599:
            self.y=0
        if self.y<0:
            self.y=599
        #deduct bullet life
        self.lifeleft-=1
#game time
def gameTime():
    sTime=time.time()-startTime
    sTime=int(sTime*10)/10
    pscreen.fontWrite(0,0,'Time:'+str(sTime))

#starfield background
def drawS():#draws stars
    star_list=[]
    numStars=100
    #random color for stars
    randR=random.randint(0,255)
    randG=random.randint(0,255)
    randB=random.randint(0,255)
    randC=(randR,randG,randB)
    #add stars to list for background
    for i in range(0,numStars):
        star_list.append((random.randint(0,799),random.randint(0,599)))
     #randomize and draw random star locations
    for i in range(0,len(star_list)-1):
        (starX,starY)=star_list[i]
        pscreen.circle(starX,starY,random.randint(1,2),randC,0)

#distance function
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
#score
Score=0
#make ship and asteroid entity
ship=Ship()
#asteroid list
asteroid_list=[]
for i in range(0,5):
    asteroid_list.append(Asteroid(x=random.randint(10,789),y=random.randint(10,589),speed=random.randint(1,5)/5,angle=random.randint(0,360)))
#bullet list
bullet_list=[]
bullet_recharge_time=1
shield_recharge_time=0
shiled_invincibility_time=2
#Load Screen
pscreen.loadScreen()
pscreen.fontSelect("Arial",18)
#Game loop
while True:
    if pscreen.keyIsPressed('escape'):
        break
    #clear Screen
    pscreen.clearScreen((0,0,0))
    #draw starField
    drawS()
    #shoot a bullet
    if pscreen.keyIsPressed('space') and time.time()>=bullet_recharge_time:
        bullet_recharge_time=time.time()+1*0.5
        #append bullet
        bullet_list.append(Bullet(ship.x+25,ship.y,ship.angle,2))
    for bullet in bullet_list:
        bullet.render()
        for bullet in bullet_list:
            if bullet.lifeleft>0:
                bullet.move()
            else:
                bullet_list.remove(bullet)
    #Collisions
    for asteroid in asteroid_list:
        for bullet in bullet_list:
            #collision between asteroid and bullet
            if bullet.lifeleft==0:
                bullet_list.remove(bullet)
            #if asteroid radius is 25
            if asteroid.radius==35:
                if distance(asteroid.x,asteroid.y,bullet.x,bullet.y)<40:
                        asteroid_list.append(Asteroid(asteroid.x,asteroid.y,radius=25,speed=random.randint(1,5)/5))
                        asteroid_list.append(Asteroid(asteroid.x,asteroid.y,radius=25,speed=random.randint(1,5)/5))
                        asteroid_list.append(Asteroid(asteroid.x,asteroid.y,radius=25,speed=random.randint(1,5)/5))
                        asteroid_list.remove(asteroid)
                        bullet_list.remove(bullet)
                        Score+=50
                        break
                #if asteroid radius is 10
            elif asteroid.radius==25:
                if distance(asteroid.x,asteroid.y,bullet.x,bullet.y)<30:
                    asteroid_list.remove(asteroid)
                    bullet_list.remove(bullet)
                    Score+=100
                    break
        #collision between ship and asteroid
        if asteroid.radius==35:
            if distance(asteroid.x,asteroid.y,ship.x,ship.y)<65 and ship.shield==False:
                ship.energy-=10
                ship.heading*=-1
                asteroid.heading*=-1
                ship.speed*=-1
                ship.shield=True
        elif asteroid.radius==25:
            if distance(asteroid.x,asteroid.y,ship.x,ship.y)<55 and ship.shield==False:
                ship.energy-=10
                ship.heading*=-1
                asteroid.heading*=-1
                ship.shield=True
    if ship.shield==True and time.time()>shield_recharge_time:
        ship.shield=False
        shield_recharge_time=time.time()+2
    #draw ship
    ship.draw_Ship()
    #draw Asteroid
    for asteroid in asteroid_list:
        asteroid.render()
    #break from loop if energy reaches 0
    if ship.energy==0:
        break
    if asteroid_list==[]:
        break
    #display time
    gameTime()
    #display energy left
    pscreen.fontWrite(0,579,"Shield Energy Left:"+str(ship.energy))
    #display Score
    pscreen.fontWrite(100,0,"Score:"+str(Score))
    #update Screen
    pscreen.updateScreen()
#Unload screen
if ship.energy==0:
    pscreen.fontWrite(375,300,"Game Over",(255,140,0))
    pscreen.fontWrite(385,325,"Score:"+str(Score),(255,140,0))
    pscreen.updateScreen()
    time.sleep(5)
else:
    pscreen.fontWrite(375,300,"Thanks for Play!",(255,140,0))
    pscreen.fontWrite(395,325,"Score:"+str(Score),(255,140,0))
    pscreen.updateScreen()
    time.sleep(5)
pscreen.unloadScreen()
                
    
