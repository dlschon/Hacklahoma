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
import Objects.info
from Objects.menus import GameMenu
from Objects.info import BuildingInfo
from Objects.info import MoneyInfo
from Objects.info import StudentInfo
from Objects.info import BuyBuilding
from Objects.info import InitialMessage
from Objects.info import PauseMenu
from Objects.info import TeacherMenu
from Objects.teacher import Teacher
from Objects.buildings.emptylot import EmptyLot
import admissions
from date import Date

# Usual pygame initialization
pygame.init()
pygame = global_vars.pygame
pygame.init()
pygame.display.set_caption('SimU')
gameDisplay = pygame.display.set_mode((1100,720))
clock = pygame.time.Clock()

map = global_vars.map
university = global_vars.university

events = []

# Push the initial message to the user
def initial_message():
    message = InitialMessage()
    university.name = message.name
    pygame.display.set_caption(university.name)

#events.append((initial_message, 0))

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
                if type(clicked) == EmptyLot:
                    BuyBuilding(clicked)
                else:
                    BuildingInfo(clicked)

            # Try clicking the menu
            clicked = gameMenu.try_click(pos)
            if clicked != -1:
                if clicked == GameMenu.PAUSE:
                    PauseMenu()
                if clicked == GameMenu.MONEY:
                    MoneyInfo()
                if clicked == GameMenu.STUDENTS:
                    StudentInfo()
                if clicked == GameMenu.TEACHERS:
                    teacher = Teacher.generate()
                    tm = TeacherMenu(teacher)


    # Draw background
    gameDisplay.fill((255,255,255))

    # Draw the map
    gameDisplay.blit(map.surface, (0,0))

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
        # Update construction projects
        global_vars.map.update_construction()

        # update finances
        global_vars.university.money += global_vars.university.calcRevenue()[0] - global_vars.university.calcExpense()[0]

        # Decrement the counter on all events
        for event in events:
            event[1] -= 1

        global_vars.university.can_hire = True

        # Evaluate school
        for student in global_vars.university.students:
            student.evalSchool()

        if global_vars.date.current == Date.fall_enrollment or global_vars.date.current == Date.spring_enrollment:
            admissions.admit_students()
    # Execute any events that are due
    for event in events:
        if event[1] <= 0:
            event[0]()
            events.remove(event)

    clock.tick(60)
