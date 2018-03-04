import pygame
import sys
from names import Names
from tileset import Tileset
import program

pygame = program.pygame
pygame.init()
gameDisplay = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()

map = program.map
mapSurface = map.get_surface()

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    # Draw background
    gameDisplay.fill((255,255,255))

    # Draw the map
    gameDisplay.blit(mapSurface, (0,0))

    pygame.display.update()
    clock.tick(60)