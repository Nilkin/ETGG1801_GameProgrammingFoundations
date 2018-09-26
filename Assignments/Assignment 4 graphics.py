# pscreen graphics assignment 4 by. Thomas Gilman

#imports for code
import pscreen
import math
import random
import time

#loading of the screen
pscreen.loadScreen()


#assigning values to white and black
#Face
pscreen.circle(200,200,50,(255,255,255),1)
#Eyes
pscreen.ellipse(175,185,10,5,(255,255,255),1)#changed it from (140,175,20,10)
pscreen.ellipse(225,185,10,5,(255,255,255),1)
pscreen.circle(175,185,2,(255,255,255),1)
pscreen.circle(225,185,2,(255,255,255),1)
#smile
pscreen.line(175,225,225,225,(255,255,255),1)#changed it from (150,250,250,250)
pscreen.line(175,225,170,230,(255,255,255),1)#changed it from (150,250,130,260)
pscreen.line(225,225,230,230,(255,255,255),1)#changed it from (250,250,270,260)
#Nose
pscreen.line(190,200,200,205,(255,255,255),1)#changed it from (170,180,200,200)
pscreen.line(190,200,205,190,(255,255,255),1)#changed it from (170,180,210,170)

#pacman
#body
pscreen.circle(400,200,25,(255,255,0),0)#changed it from (400,200,25)
#eye
pscreen.circle(400,185,3,(0,0,0),0)#changed it from (400,175,10)

#mouth
pscreen.triangle(400,200,450,225,450,175,(0,0,0),0)

#ghost
#body
pscreen.circle(700,205,25,(0,255,255),0)#changed from (700,175,25)
#deleted (pscreen.rectangle(675,200,725,175,(0,255,255),0))
pscreen.rectangle(675,225,725,200,(0,255,255),0)

#eyes
pscreen.circle(685,200,3,(0,0,0),0)#changed from (685,185,5)
pscreen.circle(715,200,3,(0,0,0),0)#changed from (715,185,5)
#mouth
pscreen.line(685,210,715,210,(0,0,0),1)
#triagle base
pscreen.triangle(675,225,675,230,680,225,(0,255,255),0)
pscreen.triangle(680,225,680,230,685,225,(0,255,255),0)
pscreen.triangle(685,225,685,230,690,225,(0,255,255),0)
pscreen.triangle(690,225,690,230,695,225,(0,255,255),0)
pscreen.triangle(695,225,695,230,700,225,(0,255,255),0)
pscreen.triangle(700,225,700,230,705,225,(0,255,255),0)
pscreen.triangle(705,225,705,230,710,225,(0,255,255),0)
pscreen.triangle(710,225,710,230,715,225,(0,255,255),0)
pscreen.triangle(715,225,715,230,720,225,(0,255,255),0)
pscreen.triangle(720,225,720,230,725,225,(0,255,255),0)


#Code to keep programm open until button:q is pressed to then unload the screen after 5sec.
while pscreen.keyIsNotPressed("q"):
    pscreen.updateScreen()
pscreen.unloadScreen()

