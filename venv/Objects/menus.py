# import global_vars
import pygame
from pygame import Rect
from tkinter import *
from tkinter import messagebox
import global_vars

# pygame = global_vars.pygame

LIGHT_GREEN = (73, 164, 100)
LIGHT_RED = (255,100,100)
LIGHT_GREY = (100,100,100)
BLACK = (0,0,0)

class FillBar:
    def __init__(self, xy, w, h, percent, bg_color, fill_color, font_size=20, font_color=(BLACK), font=None):
        self.xy = xy
        self.x, self.y = self.xy
        self.w = w
        self.h = h
        self.percent = percent
        self.bg_color = bg_color
        self.fill_color = fill_color
        self.font_size = font_size
        self.font_color = font_color
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.w, self.h)) #Background
        pygame.draw.rect(screen, self.fill_color, (self.x, self.y + 2, self.w * self.percent, self.h - 4)) #Fill

class MenuItem(pygame.font.Font):
    def __init__(self, text, xy=(0, 0), font_size=20, font_color=(0, 0, 0), font=None):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x, self.pos_y = xy
        self.position = xy

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

    def is_mouse_selection(self):
        posx, posy = pygame.mouse.get_pos()
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) \
            and (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False


class Shape:
    def __init__(self, color=(100,100,100),xy=(0,0), w=0, h=0, id=0):
        self.color = color
        self.w = w
        self.h = h
        self.xy = xy
        self.id = id
        self.circleRect = Rect(xy[0]-w, xy[1]-w, w*2, w*2)

    def get_shape(self):
        x, y = self.xy
        return (x, y, self.w, self.h)

class GameMenu():

    PAUSE = 0
    MONEY = 1
    TEACHERS = 2
    STUDENTS = 3

    ids = ["Pause", "Money", "Teachers", "Students"]

    def set_items(self):
        self.items = []
        dateText = MenuItem("Date: " + global_vars.date.get_month_name(), (20, self.scr_height - 40))
        self.items.append(dateText)
        moneyText = MenuItem("Money: $" + str(global_vars.university.money), (20, self.scr_height - 15))
        self.items.append(moneyText)
        enrollmentText = MenuItem("Enrollment: " + str(len(global_vars.university.students)), (320, self.scr_height - 40))
        self.items.append(enrollmentText)
        incomeText = MenuItem("Income/mo: $" + str(global_vars.university.calcRevenue()[0]+global_vars.university.calcExpense()[0]), (320, self.scr_height - 15))
        self.items.append(incomeText)
        moraleText = MenuItem("Campus Morale: " , (520, self.scr_height - 40))
        self.items.append(moraleText)
        reputationText = MenuItem("Reputation: " + str(global_vars.university.reputation), (520, self.scr_height - 15))
        self.items.append(reputationText)

    def __init__(self, screen):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        self.fb = FillBar((20, self.scr_height - 45), 150, 20, 0.0, LIGHT_GREY, LIGHT_GREEN, 60, LIGHT_RED)

        # Array of menu items (text) to be displayed on screen
        self.set_items()

        # Array of rects to be drawn on screen
        self.rects = []
        footerBackground = Shape(LIGHT_RED, (0, self.scr_height-50), self.scr_width, 50)
        self.rects.append(footerBackground)
        leftBar = Shape(LIGHT_RED, (0,0), 20, self.scr_height)
        self.rects.append(leftBar)

        # Array of circles to be drawn on screen
        self.circles = []
        pauseCircle = Shape(LIGHT_GREY, (25,50), 20, id=GameMenu.PAUSE)
        self.circles.append(pauseCircle)
        moneyCircle = Shape(LIGHT_GREY, (25,100), 20, id=GameMenu.MONEY)
        self.circles.append(moneyCircle)
        teachersCircle = Shape(LIGHT_GREY, (25,150), 20, id=GameMenu.TEACHERS)
        self.circles.append(teachersCircle)
        studentsCircle = Shape(LIGHT_GREY, (25,200), 20, id=GameMenu.STUDENTS)
        self.circles.append(studentsCircle)

        # Array of icons to be drawn on the screen
        self.icons = []
        pauseIcon = pygame.image.load('Resources/icons/pause-button.png')
        pauseIcon = pygame.transform.scale(pauseIcon, (30,30))
        self.icons.append(pauseIcon)
        moneyIcon = pygame.image.load('Resources/icons/money.png')
        moneyIcon = pygame.transform.scale(moneyIcon, (30,30))
        self.icons.append(moneyIcon)
        teachersIcon = pygame.image.load('Resources/icons/teachers.png')
        teachersIcon = pygame.transform.scale(teachersIcon, (30,30))
        self.icons.append(teachersIcon)
        studentsIcon = pygame.image.load('Resources/icons/students.png')
        studentsIcon = pygame.transform.scale(studentsIcon, (30,30))
        self.icons.append(studentsIcon)

    def try_click(self, pos):
        for circle in self.circles:
            if circle.circleRect.collidepoint(pos):
                return circle.id
        return -1

    def drawAll(self):
        for rect in self.rects:
            pygame.draw.rect(self.screen, rect.color, rect.get_shape())
        for circle in self.circles:
            pygame.draw.circle(self.screen, circle.color, circle.xy, circle.w)
        x = 10;
        y = 35
        for icon in self.icons:
            self.screen.blit(icon, (x, y))
            y += 50

        self.fb.draw(self.screen)

        for item in self.items:
            if item.is_mouse_selection():
                item.set_font_color((255, 0, 0))
                item.set_italic(True)
            else:
                item.set_font_color((255, 255, 255))
                item.set_italic(False)
            self.screen.blit(item.label, item.position)

    def run(self, pos, progress):
            self.set_items()
            self.fb.percent = progress

            # Redraw the background
            hovering = None
            for rect in self.rects:
                pygame.draw.rect(self.screen, rect.color, rect.get_shape())

            self.drawAll()
            for circle in self.circles:
                pygame.draw.circle(self.screen, circle.color, circle.xy, circle.w)

                if circle.circleRect.collidepoint(pos):
                    hovering = GameMenu.ids[circle.id]

            x = 10; y = 35
            for icon in self.icons:
                self.screen.blit(icon, (x,y))
                y+=50
            for item in self.items:
                if item.is_mouse_selection():
                    item.set_font_color((255, 0, 0))
                    item.set_italic(True)
                else:
                    item.set_font_color((255, 255, 255))
                    item.set_italic(False)
                self.screen.blit(item.label, item.position)
            pygame.display.flip()

            return hovering
