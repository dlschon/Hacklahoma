import pygame
import sys
from names import Names
from tileset import Tileset
import global_vars
from tkinter import *
from tkinter import messagebox
import os

root = Tk()

embed = Frame(root, width=1200, height=800)
embed.pack()
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save Game", command=donothing)
filemenu.add_command(label="Load Game", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# Tell pygame's SDL window which window ID to use
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
# Show the window so it's assigned an ID.
root.update()

# Usual pygame initialization
pygame.init()

pygame = global_vars.pygame
pygame.init()
gameDisplay = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()

map = global_vars.map
mapSurface = map.get_surface()

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

    # Draw background
    gameDisplay.fill((255,255,255))

    # Draw the map
    gameDisplay.blit(mapSurface, (0,0))

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