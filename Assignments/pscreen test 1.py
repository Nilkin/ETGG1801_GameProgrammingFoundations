# pscreen Test Program

import pscreen
import time
import random

pscreen.loadScreen()

pscreen.circle(200,200,100)
pscreen.circle(400,400,100,(0,0,255),5)
pscreen.circle(300,300,100,(0,0,254),0)

pscreen.line(200,200,400,400,(255,0,0),5)

i=0
while i<100:
    rand_x = random.randint(0,799)
    rand_y = random.randint(0,599)
    rand_radius = random.randint(20,100)
    rand_r = random.randint(0,255)
    rand_g = random.randint(0,255)
    rand_b = random.randint(0,255)
    pscreen.circle(rand_x,rand_y,rand_radius)
    i+=1
    

while pscreen.keyIsNotPressed("q"):
    pscreen.updateScreen()
time.sleep(5)

pscreen.unloadScreen()
