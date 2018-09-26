#particlefx.py
import pygame
import math
import random

class Emitter(object):
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.particleList = []
    def explode(self):
        self.x, self.y = pygame.mouse.get_pos()
        bob = Particle(self.x,self.y)
        self.particleList.append(bob)
    def update(self,elapsedTime):
        for spark in particleList:
            spark.move(elapsedTime)
            spark.updateLife(elapsedTime)
    def draw(self,screen)
        for spark in particleList:
            if spark.life > 0:
                spark.draw(screen)
        
class Particle(object):
    #x,y,vx,vy,angle,ay,life
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angle = random.randint(0,359)
        #velocity total = 5
        self.vx = 5*math.cos(math.radans(self.angle))
        self.vy = 5*math.sin(math.radans(self.angle))
        self.ay = 9.8
        self.life = random.randint(10,30)
    def move(self,elapsedTime):
        self.x += self.vx*elpasedTime
        self.vy += self.ay*elapsedTime
        self.y += self.vy*elapsedTime
    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), (self.x,self.y), 5, 0)
    def updateLife(self,elapsedTime):
        self.life -= elapsedTime
