import pygame
import sys
from names import Names
from tileset import Tileset
import global_vars
from tkinter import *
from tkinter import messagebox
import os
from pygame import Rect

# Usual pygame initialization
pygame.init()

pygame = global_vars.pygame
pygame.init()
gameDisplay = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()

map = global_vars.map
mapSurface = map.get_surface()
university = global_vars.university

events = []

# Push the initial message to the user
def initial_message():
    Tk().wm_withdraw() #to hide the main window
    messagebox.showinfo('Info','Congratulations! You have been elected President of a small land-grant University! Invest your resources wisely and grow your University!')
events.append((initial_message, 0))

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked = global_vars.map.try_click(pos)

            if clicked != None:
                messagebox.showinfo('Info', clicked.name)


    # Draw background
    gameDisplay.fill((255,255,255))

    # Draw the map
    gameDisplay.blit(mapSurface, (0,0))

    # Hover text
    pos = pygame.mouse.get_pos()
    hovering = global_vars.map.try_click(pos)
    if hovering != None:
        pygame.draw.rect(gameDisplay, (255,255,255), Rect(pos[0], pos[1], 50, 20))
        #label = global_vars.font.render(hovering.name, 1, (255, 255, 0))
        #gameDisplay.blit(label, pos)

    pygame.display.update()
    progress, new_month = global_vars.date.increment_time()
    # The month has rolled over, do monthly events
    if new_month:
        # Decrement the counter on all events
        for event in events:
            event[1] -= 1

    # Execute any events that are due
    for event in events:
        if event[1] <= 0:
            event[0]()
            events.remove(event)

    clock.tick(60)