import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    pygame.display.update()
    clock.tick(60)