#bullets example: dynamic game object creation
import pscreen
import random
import time

def distance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

#initialize pscreen
pscreen.loadScreen()
pscreen.fontSelect()

#initialize game variables
bullet_list=[]
bullet_recharge_time=0

#start the game loop
while True:
    #check for exit
    if pscreen.keyIsPressed("escape"):
        break
    
    #check to see if we want to create a bullet
    if pscreen.keyIsPressed("space") and time.time()>=bullet_recharge_time:
        bullet_recharge_time = time.time()+0.1 #calculate time when gun is next ready
        #create a bullet
        bullet_list.append([0,300+random.randint(-15,15)])
    
    #move bullets
    for bullet in bullet_list:
        bullet[0]+=1    
    
    #render section
    pscreen.clearScreen((0,0,0))    

    #draw bullets
    for bullet in bullet_list:
        (bulletx,bullety)=bullet
        pscreen.circle(bulletx,bullety,5,(255,0,0),0)

    #check for bullets that have left the screen
    for bullet in bullet_list:
        if bullet[0]>799:
            bullet_list.remove(bullet)

    #check for bullet collisions with circle
    bullets_to_remove=[]        
    for bullet in bullet_list:
        if distance(mx,my,bullet[0],bullet[1]) <= 30+5:
            #mark bullets to be removed
            bullets_to_remove.append(bullet)

    #remove marked bullets        
    for bullet in bullets_to_remove:
        bullet_list.remove(bullet)

    #draw player
    mx=pscreen.mouseGetX()
    my=pscreen.mouseGetY()
    pscreen.circle(mx,my,30,(0,0,255))

    #display number of bullets
    pscreen.fontWrite(0,0,str(len(bullet_list)))
    pscreen.updateScreen()
    
pscreen.unloadScreen()
