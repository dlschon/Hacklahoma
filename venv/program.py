from Objects.map import Map
from names import Names
import pygame
from tileset import Tileset

# Important program objects
# Object that generates human names
names = Names()
# Our pygame object
pygame = pygame
# Tileset of game graphics
tileset = Tileset(pygame, './Resources/city_tiles.png', 8, 21)
# Standard size of one tile
tile_size = 8
# How much we scale each tile
tile_scale = 2
# Game map
map = Map(pygame, tile_size*tile_scale)
