#Etgg 1801-02
#Thomas Gilman
#More with Pygame notes

#Pygame: More with surfaces:
    #Surface Transforms:
        #new surface#pygame.transform.scale(sourceSurface,(width,height)<-size to scale to)
            #*usefulmfor sizing or representing distance.
    #pygame.transform.rotate(sourceSurface,angle):
        #*returns a new source that has been rotated(In degrees).
    #New surface=pygame.transform.flip(sourceSurface,True/False(x-axis),True/False(y-axis))
        #*useful for left/right sprite animations
    #New Surface2=pygame.transform.rotoZoom(sourceSurface,angle,zoomfactor(size multiplier,1.0=no change))

#Pygame example 2

import pygame
import time

pygame.init()

disp_surf=pygame.display.set_mode((800,600),pygame.SWSURFACE,24)

patty_surf=pygame.image.load("fsm2.jpg")

#blitting from upper-left corner
for i in range(0,720):
    disp_surf.fill((0,0,0))
    new_surf=pygame.transform.rotate(patty_surf,i)
    disp_surf.blit(new_surf,(100,100))
    pygame.display.flip()

#blitting from center of image
for i in range(0,720):
    new_surf=pygame.transform.rotate(patty_surf,i)
    disp_surf.fill((0,0,0))
    disp_surf.blit(new_surf,(100-new_surf.get_width()/2,100-new_surf.get_height()/2))
    pygame.display.flip()

for i in range(0,720):
    new_surf=pygame.transform.rotozoom



pygame.display.flip()
time.sleep(5)

pygame.display.quit()

#Pygame Sounds:
    #Two types of sounds:
        #*Sound effects
        #*Background Music
    #pygame.mixer.set_num_channels(8)<-number of simultaneous sounds.
#Load a sound:
    #sound_snd=pygame.mixer.Sound("sound.file")
#Playing a sound:
    #sound_snd.play()
#Adjust sound volume
    #sound_snd.set_volume(0.0-1.0)
    #sound_snd.get_volume()
#Fade out sound
    #sound_snd.fade_out(500(number of milliseconds to fade over))
#Stop the sound
    #sound_snd.stop()<-stop immediately
#get length of sound
    #sound_snd.get_length()<-return length in seconds
#Music:
    #pygame.mixer.music.load("music.mp3"(file name))
#play the music
    #pygame.mixer.music.play(loops=(-1=forever),startpos=0.0(#seconds in song))
#Stop the music
    #pygame.mixer.music.stop()
#fade out music
    #pygame.mixer.music.fade_out(500)
#set volume
    #pygame.mixer.music.set_volume(1.0)
#pause/unpause musice
    #pygame.mixer.music.pause()
    #pygame.mixer.music.unpause()
#Que music
    #pygame.mixer.music.queue("BossMusic.mp3")
#rewind music
    #pygame.mixer.music.rewind()
#pygame.mixer.fade_out(500)
#pygame.mixer.pause()
#pygame.mixer.unPause()
#pygame.mixer.stop()

#Input with Pygame:
    #Mouse:
        #*(mx,my)=pygame.mouse.get_pos()
            #returns the x, and y of the mouse.
        #*pygame.mouse.set_visible(True/False)
            #set mouse pointer visibility
        #(LB,MB,RB)=pygame.mouse.get_pressed()
            #*^^each is true or false.
        #pygame.mouse.set_pos((x,y))
    #Keyboard Input:
        #pygame.event.pump()<-allows pygame to receive events from the O.S.
                #Must be called regularly, usually called in the game loop
        #pygame.key.get_pressed()<-returns a giant tuple of all keys & their states
                #Position in tuple determines key.
                #difficult to use.
        #pygame.key.name(number)<-returns keyname of position specified
#keyboard helper functions:
    #def keyGetPressedList():
        #pygame.event.pump()
        #pressed=pygame.key.get_pressed()
        #result=[]
        #for i in range(0,len(pressed)):
            #if pressed[i]=0:
                #result.append(pygame.key.name(i))
        #return result

    #def keyIsPressed(keySymbol):
        #if keySymbol in keyGetPressedList():
            #return True
        #else:
            #return False

    #def keyIsNotPressed(keySymbol):
        #if keySymbol not in keyGetPressedList():
            #return True
        #else:
            #return False
        
