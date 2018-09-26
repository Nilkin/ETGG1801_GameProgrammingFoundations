#Graphics list example

import random
import pscreen
import time

def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**.05

pscreen.loadScreen()
pscreen.fontSelect()

bullet_list=[]

while True:
    if pscreen.keyIsPressed("escape"):
        break

    pscreen.clearScreen((0,0,0))
    #check to see if we want to create a bullet
    if pscreen.keyIsPressed("space") and last_space_not_pressed==True:
        #set recharge time
       if last_space_not_pressed==True:
        #create a bullet
        bullet_list.append([0,300+random.randint(-150,150)])
        last_space_not_pressed=False
    else:
        last_space_not_pressed=True

    #if pscreen.keyIsPressed("space") and time.time()>=bullet_recharge_time:
        #set recharge time
     #   bullet_recharge_time=time.time()+1
        
        #create a bullet
      #  bullet_list.append([0,300+random.randint(-150,150)])
    #move bullets
    for bullet in bullet_list:
        bullet[0]+=1

    mx=pscreen.mouseGetX()
    my=pscreen.mouseGetY()

    
    #draw bullets
    for bullet in bullet_list:
        (bx,by)=bullet
        pscreen.circle(bx,by,5,(255,0,0),0)

    #check for bullets that have left the screen
    for bullet in bullet_list:
        if bullet[0]>799:
            bullet_list.remove(bullet)

    #check for bullet collision with circle
    for bullet in bullet_list:
        if distance(mx,my,bullet[0],bullet[1]) <=30+5:
            bullet_list.remove(bullet)

    pscreen.circle(mx,my,30,(0,0,255),0)
    
    #render screen
    pscreen.fontWrite(0,0,str(len(bullet_list)))
    pscreen.updateScreen()

pscreen.unloadScreen

