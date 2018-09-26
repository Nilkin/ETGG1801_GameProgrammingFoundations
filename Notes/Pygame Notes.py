#Thomas Gilman
#12/2/15
#Pygame Notes

#pscreen- a wrapper module for other, more complex modules.
#Pygame is one of these modules.
#Pygame has a website-www.pygame.org
#Pygame is a wrapper for S.D.L.

#Using Pygame:
#Import pygame
#pygame.init()#-must be called before we do anything else with pygame.

#surfaces:
    #*Most grahpical functionality in pygame uses surfaces.
    #*a surface is a pygame object designed to store graphical data.
    #*we can do many things to pygame surfaces: draw lines, circles,pixels,rectangles,copy images onto, etc..
    #*we can make many surfaces & they can be of different sizes.
    #*One surface is special-the display surface:we create the display surface by using: {pygame.display.set_mode()}
    #*Images are loaded as surfaces, fonts are rendered on surfaces, drawing is done on surfaces, etc..

#The display surface is controlled by the {display object}.
#screen=pygame.display.set_mode((800,600),pygame.SWSURFACE,24)#(resolution,flags,bits/pixel)
#^^Returns the display surface.
#Useful Functions:
    #*pygame.display.list_mode()<- returns a list of all the supported resolutions.
    #*pygame.display.flip()<- updates the screen[like pscreen.updateScreen()]
    #*pygame.display.update((10,10,100,100)) <- only updates a section of the screen()
    #*pygame.display.quit() <-closes the window[like pscreen.unloadScreen()].
    #to chang the icon in the top left corner *pygame.display.set_caption("my game").

#pygame example 1
import pygame
import random
import time
import pygame.gfxdraw
#initalize pygame
pygame.init()
#creates the display screen
screen=pygame.display.set_mode((800,600),pygame.SWSURFACE,24)
#changes the caption
pygame.display.set_caption("Thomas's pygame 1st example")
#load image
fsm=pygame.image.load("fsm.jpg")
#fills the surface with a color
screen.fill((25,78,50))
#font
font=pygame.font.SysFont("Arial",24)
font_surface=font.render("Game Over",0,(255,0,0),(25,78,50))
#blit image to screen
screen.blit(fsm,(400,300))
#blit font
screen.blit(font_surface,(300,200))
#draw line
pygame.draw.line(screen,(245,234,255),(0,0),(799,599),1)
#draw circle
pygame.gfxdraw.circle(screen,100,100,50,(20,50,60,0))
#draw polygon
pygame.draw.polygon(screen,(255,255,255),[(100,200),(300,100),(200,450)],0)
#updates screen
pygame.display.flip()
time.sleep(5)
#unloads screen
pygame.display.quit()

#fsm=pygame.image.load("fsm.jpg")
#^returns a surface that contains the loaded image.
#font=pygame.font.sysFont("Arial",20) or<- registered font name
#font=pygame.font.Font("somefont.ttf",20)<- font file
#font_surface=font.render("Game Over",0,(255,0,0),(0,0,0))<-returns a surface that contains the image of the text.
#                         ^string    ^anti-aliase ^fore_ground_color ^optional background color.
#Blank surfaces:
    #*surface1=pygame.Surface((200,100))<-width of surface to create.
#To do something with the surfaces:
    #*Every surface has a blit object function:
    #Blit=block.image.transfer
    #destination surface-> Screen.blit(fsm[source surface],(100,100)[offset location to blit to],(10,10,20,20)[optional source rectangle])
#Drawing: Pygame has functions that allow drawing on any surface.
    #*Pygame.draw.line(screen,color,start position pair(x,y),end position pair(x,y),width)
    #*Pygame.draw.circle(screen,color,center position pair,radius,width)
