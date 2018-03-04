import pygame
pygame.init()

LIGHT_GREEN = (100,255,100)
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
        txt = MenuItem("60%", (self.x + self.w / 2, self.y + self.h / 2), self.font_size, self.font_color, self.font) #Text
        txt.set_position(txt.pos_x - txt.width / 2, txt.pos_y - txt.height / 2)
        screen.blit(txt.label, txt.position)

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
    def __init__(self, color=(100,100,100),xy=(0,0), w=0, h=0):
        self.color = color
        self.w = w
        self.h = h
        self.xy = xy

    def get_shape(self):
        x, y = self.xy
        return (x, y, self.w, self.h)

class GameMenu():
    def __init__(self, screen, bg_color=(0,0,0)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        # Array of menu items (text) to be displayed on screen
        self.items = []
        dateText = MenuItem("Date", (20, self.scr_height - 40))
        self.items.append(dateText)
        moneyText = MenuItem("Money", (20, self.scr_height - 15))
        self.items.append(moneyText)
        enrollmentText = MenuItem("Enrollment", (320, self.scr_height - 40))
        self.items.append(enrollmentText)
        incomeText = MenuItem("Income/mo.", (320, self.scr_height - 15))
        self.items.append(incomeText)
        moraleText = MenuItem("Campus Morale", (520, self.scr_height - 40))
        self.items.append(moraleText)
        reputationText = MenuItem("Reputation", (520, self.scr_height - 15))
        self.items.append(reputationText)

        # Array of rects to be drawn on screen
        self.rects = []
        footerBackground = Shape(LIGHT_RED, (0, self.scr_height-50), self.scr_width, 50)
        self.rects.append(footerBackground)
        leftBar = Shape(LIGHT_RED, (0,0), 20, self.scr_height)
        self.rects.append(leftBar)

        # Array of circles to be drawn on screen
        self.circles = []
        buildCircle = Shape(LIGHT_GREY, (25,50), 20)
        self.circles.append(buildCircle)
        moneyCircle = Shape(LIGHT_GREY, (25,100), 20)
        self.circles.append(moneyCircle)
        programsCircle = Shape(LIGHT_GREY, (25,150), 20)
        self.circles.append(programsCircle)
        teachersCircle = Shape(LIGHT_GREY, (25,200), 20)
        self.circles.append(teachersCircle)
        studentsCircle = Shape(LIGHT_GREY, (25,250), 20)
        self.circles.append(studentsCircle)

        # Array of icons to be drawn on the screen
        self.icons = []
        buildIcon = pygame.image.load('../Resources/icons/build.png')
        buildIcon = pygame.transform.scale(buildIcon, (30,30))
        self.icons.append(buildIcon)
        moneyIcon = pygame.image.load('../Resources/icons/money.png')
        moneyIcon = pygame.transform.scale(moneyIcon, (30,30))
        self.icons.append(moneyIcon)
        programsIcon = pygame.image.load('../Resources/icons/programs.png')
        programsIcon = pygame.transform.scale(programsIcon, (30,30))
        self.icons.append(programsIcon)
        teachersIcon = pygame.image.load('../Resources/icons/teachers.png')
        teachersIcon = pygame.transform.scale(teachersIcon, (30,30))
        self.icons.append(teachersIcon)
        studentsIcon = pygame.image.load('../Resources/icons/students.png')
        studentsIcon = pygame.transform.scale(studentsIcon, (30,30))
        self.icons.append(studentsIcon)

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
        for item in self.items:
            if item.is_mouse_selection():
                item.set_font_color((255, 0, 0))
                item.set_italic(True)
            else:
                item.set_font_color((255, 255, 255))
                item.set_italic(False)
            self.screen.blit(item.label, item.position)
        fb = FillBar((200,200), 300, 50, 0.7, LIGHT_GREY, LIGHT_GREEN, 60, LIGHT_RED)
        fb.draw(self.screen)

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
            # Redraw the background
            self.screen.fill(self.bg_color)
            self.drawAll()
            pygame.display.flip()

if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen)
    gm.run()
