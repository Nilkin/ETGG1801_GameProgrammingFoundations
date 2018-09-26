#program 3 draws objects on screen if key is pressed
#ETGG 1801-01 by. Thomas Gilman

#imports
import pscreen
import random
b=(0,0,255)
black=(0,0,0)
white=(255,255,255)
def drawFace(x,y,randMood):
            #face
            pscreen.circle(x,y,20,c,0)
            #whites of eyes
            pscreen.circle(x-5,y-5,5,white,0)
            pscreen.circle(x+5,y-5,5,white,0)
            #color of eyes
            pscreen.circle(x-5,y-5,2,b,0)
            pscreen.circle(x+5,y-5,2,b,0)
            #pupils
            pscreen.circle(x-5,y-5,1,(0,0,0),0)
            pscreen.circle(x+5,y-5,1,(0,0,0),0)
            #nose
            pscreen.line(x-2,y,x+3,y+2,(0,0,0),1)
            pscreen.line(x-2,y,x+3,y-2,(0,0,0),1)
            #Mouth
            if randMood == "happy":
                pscreen.line(x-5,y+5,x+5,y+5,black)
                pscreen.line(x-5,y+5,x-7,y+3,black)
                pscreen.line(x+5,y+5,x+7,y+3,black)
            elif randMood == "nuetral":
                pscreen.line(x-5,y+5,x+5,y+5,black)
            elif randMood == "sad":
                pscreen.line(x-5,y+5,x+5,y+5,black)
                pscreen.line(x-5,y+5,x-7,y+8,black)
                pscreen.line(x+5,y+5,x+7,y+8,black)
#loading screen
pscreen.loadScreen()

#moods
m=["happy","sad","nuetral"]

#loop
while True:
    #values
    randMood=m[random.randint(0,len(m)-1)]
    x=random.randint(0,799)#random x cordinate
    y=random.randint(0,799)#random y cordinate
    randR=random.randint(5,255)#random Red value
    randG=random.randint(5,255)#random Green value
    randB=random.randint(5,255)#random Blue value
    c=(randR,randG,randB)#random colors
    #pressing c prints circles on the screen
    if pscreen.keyIsPressed("c"):
        pscreen.circle(x,y,20,c)
    #pressing s prints squares on the screen
    if pscreen.keyIsPressed("s"):
        pscreen.rectangle(x,y,x-20,y-20,c)
    #pressing f prints faces with moods on the screen
    if pscreen.keyIsPressed("f"):
        
        #draws the defined face
        drawFace(x,y,randMood)
            #clear screen to a random color
    if pscreen.keyIsPressed("e"):
        pscreen.clearScreen(c)
        #random diamonds
    if pscreen.keyIsPressed("d"):
        pscreen.triangle(x,y,x-6,y,x-3,y-10,c)
        pscreen.triangle(x,y,x-6,y,x-3,y+10,c)
    if pscreen.keyIsPressed("escape"):
        break
    pscreen.updateScreen()

#unloadScreen
pscreen.unloadScreen()
            
        
        
