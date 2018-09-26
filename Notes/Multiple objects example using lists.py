#multiple objects example using lists
import pscreen
import random

pscreen.loadScreen()


star_list=[]
numStars=200

for i in range(0,numStars):
    star_list.append((random.randint(0,799),random.randint(0,599)))

while True:
    randR=random.randint(0,255)
    randG=random.randint(0,255)
    randB=random.randint(0,255)
    randC=(randR,randG,randB)
    if pscreen.keyIsPressed("escape"):
        break
    if pscreen.keyIsPressed("a"):
        star_list.append((random.randint(0,799),random.randint(0,599)))
    if pscreen.keyIsPressed("c"):
        star_list=[]
        

    #render
    pscreen.clearScreen((0,0,0))

    #drawStar
    for i in range(0,len(star_list)-1):
        (starX,starY)=star_list[i]
        pscreen.circle(starX,starY,random.randint(1,3),randC,0)

    pscreen.updateScreen()

pscreen.unloadScreen()
