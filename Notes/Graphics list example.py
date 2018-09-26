#Graphics list example

import random
import pscreen

pscreen.loadScreen
pscreen.fontSelect()

bullet_list=[]

while True:
    if pscreen.keyIsPressed("escape"):
        break

    pscreen.clearScreen((0,0,0))
    #check to see if we want to create a bullet
    if pscreen.keyIsPressed("space"):
        #create a bullet
        bullet_list.append([0,300+random.randint(-150,150)])
    #move bullets
    for bullet in bullet_list:
        bullet[0]+=1

    #draw bullets
    for bullet in bullet_list:
        (bx,by)=bullet
        pscreen.circle(bx,by,5,(255,0,0),0)

    #check for bullets that have left the screen
    for bullet in bullet_list:
        if bullet[0]>799:
            bullet.remove(bullet)
        
    #render screen
    pscreen.fontWrite(0,0,str(len(bullet_list)))
    pscreen.updateScreen()

pscreen.unloadScreen
