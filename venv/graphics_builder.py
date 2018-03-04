# Supplementary program that lets us construct image files based on our tileset
import pygame
import sys
from names import Names
from tileset import Tileset
import pickle

import tkinter as tk
from tkinter import filedialog

pygame.init()
gameDisplay = pygame.display.set_mode((800,672))
clock = pygame.time.Clock()

WHITE = (255,255,255)
GREY = (200,200,200)
ORANGE = (255,127,80)

tilesPallet = pygame.image.load('./Resources/city_tiles.png')
tilesPallet = pygame.transform.scale(tilesPallet, (256, 672))

pallet_width = 8
pallet_height = 21
tile_size = 256/8

editor_size = 10

selected_tile = (0,0)

tileMatrix = []
for x in range(editor_size):
    tileMatrix.append([])
    for y in range(editor_size):
        tileMatrix[x].append((0,0))

tileset = Tileset(pygame, './Resources/city_tiles.png', pallet_width, pallet_height)

start_x = (pallet_width+1)*tile_size

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # If we clicked on the pallet, change the selected tile
            if (pos[0] < pallet_width*tile_size):
                selected_tile = (int(pos[0]/tile_size), int(pos[1]/tile_size))

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if (pos[0] > start_x and pos[0] < start_x + 10*tile_size and pos[1] > 0 and pos[1] < 10*tile_size):
                clicked_cell = (int((pos[0]-start_x)/tile_size), int(pos[1]/tile_size))
                tileMatrix[clicked_cell[0]][clicked_cell[1]] = selected_tile

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                root = tk.Tk()
                root.withdraw()

                f = filedialog.asksaveasfile()
                if not(f is None):
                    f.write(str(pickle.dumps(tileMatrix)))
                f.close()

            if event.key == pygame.K_ESCAPE:
                root = tk.Tk()
                root.withdraw()

                f = filedialog.askopenfile()
                if not(f is None):
                    tileMatrix = pickle.loads(eval(f.read()))
                f.close()

    pygame.display.update()

    # Draw background
    gameDisplay.fill((255,255,255))

    # Draw the pallet
    gameDisplay.blit(tilesPallet, (0,0))

    # Draw an outline around the selected tile
    pygame.draw.rect(gameDisplay, ORANGE, (selected_tile[0]*tile_size, selected_tile[1]*tile_size, tile_size, tile_size), 2)

    # Draw the tile matrix
    x = 0
    y = 0

    for y in range(editor_size):
        for x in range(editor_size):
            cell = tileMatrix[x][y]
            gameDisplay.blit(pygame.transform.scale(tileset.get_tile(cell), (int(tile_size), int(tile_size))), (start_x + x*tile_size, y*tile_size))

    clock.tick(60)

