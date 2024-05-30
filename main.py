import pygame
from starfield import *

screen = pygame.display.set_mode([1100,1100])

stars = []
for i in range(250):
    stars.append(Starfield(screen))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    for i in range(len(stars)):
        stars[i].update()





    pygame.display.update()

pygame.quit()