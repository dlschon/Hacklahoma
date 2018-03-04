import pygame
import sys
from names import Names
from tileset import Tileset
import global_vars
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog;
import os
from pygame import Rect
from Objects.menus import MenuItem
from Objects.menus import GameMenu
from Objects.info import BuildingInfo

# Usual pygame initialization
pygame.init()
pygame = global_vars.pygame
pygame.init()
pygame.display.set_caption('University Sim')
gameDisplay = pygame.display.set_mode((1100,720))
clock = pygame.time.Clock()

map = global_vars.map
mapSurface = map.get_surface()
university = global_vars.university

events = []

# Push the initial message to the user
def initial_message():
    Tk().wm_withdraw() #to hide the main window
    messagebox.showinfo('Info','Congratulations! You have been elected President of a small land-grant University! Invest your resources wisely and grow your University!')
    university.name = simpledialog.askstring('Prompt', 'What is your University called?')
    pygame.display.set_caption(university.name)

events.append((initial_message, 0))

gameMenu = GameMenu(gameDisplay)

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # Try clicking the map
            clicked = global_vars.map.try_click(pos)
            if clicked != None:
                BuildingInfo(clicked)

            # Try clicking the menu
            clicked = gameMenu.try_click(pos)
            if clicked != -1:
                pass

    # Draw background
    gameDisplay.fill((255,255,255))

    # Draw the map
    gameDisplay.blit(mapSurface, (0,0))

    # Hover text
    pos = pygame.mouse.get_pos()
    hovering = global_vars.map.try_click(pos)
    if hovering != None:
        pygame.draw.rect(gameDisplay, (255,255,255), Rect(pos[0], pos[1], 125, 20))
        item = MenuItem(hovering.name, pos)
        gameDisplay.blit(item.label, (pos[0]+20, pos[1]))

    # Increment time
    progress, new_month = global_vars.date.increment_time()

    # Draw the Game menu
    hovering = gameMenu.run(pos, progress)
    if hovering != None:
        pygame.draw.rect(gameDisplay, (255,255,255), Rect(pos[0], pos[1], 125, 20))
        item = MenuItem(hovering, pos)
        gameDisplay.blit(item.label, (pos[0]+20, pos[1]))

    pygame.display.update()
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