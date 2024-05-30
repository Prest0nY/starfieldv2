import random
import pygame

class Starfield():

    def __init__(self,screen):

        self.screen = screen
        self.y = random.randint(0,1100)
        self.x = random.randint(0,1100)
        self.z = 1100
        self.color = [252, 252, 252]
        self.size = 1



    def circles(self):
        pygame.draw.circle(self.screen,(self.color),(self.sx, self.sy),self.size)

    def starsGoingOut(self):
        self.sx = ((self.x / self.z) - 0) / (1 - 0) * (self.x - 0) + 0
        self.sy = ((self.y / self.z) - 0) / (1 - 0) * (self.y - 0) + 0
        self.z -= 1
        if self.z == 0:
            self.z += 1

    def update(self):
        self.starsGoingOut()
        self.circles()