import pygame
import sys
from names import Names

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

names = Names()

print(names.generate_name_full_male())
print(names.generate_name_full_male())
print(names.generate_name_full_male())
print(names.generate_name_full_female())
print(names.generate_name_full_female())
print(names.generate_name_full_female())

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    pygame.display.update()
    clock.tick(60)