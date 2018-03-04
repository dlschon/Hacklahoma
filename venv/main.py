import pygame
import sys
from names import Names

pygame.init()
gameDisplay = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()

# Class that contains vital program data
class Program:
    names = Names()

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    pygame.display.update()
    clock.tick(60)