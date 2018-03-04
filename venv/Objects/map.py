from Objects.buildings.emptylot import EmptyLot
from Objects.buildings.lecturehall import LectureHall
from Objects.buildings.library import Library
from Objects.buildings.researchlab import ResearchLab
from Objects.buildings.stadium import Stadium
from Objects.buildings.studenthousing import StudentHousing
from Objects.buildings.studentunion import StudentUnion
from Objects.buildings.dininghall import DiningHall
from Objects.buildings.construction import Construction
from Objects.sprite import Sprite
import global_vars
import random
from pygame import Rect

class Map:

    EMPTY_LOT = 0
    LECTURE_HALL = 1
    LIBRARY = 2
    RESEARCH_LAB = 3
    STADIUM = 4
    STUDENT_HOUSING = 5
    STUDENT_UNION = 6

    def __init__(self, pygame, tile_size):
        self.constructions = []
        self.rects = []
        self.pygame = pygame
        self.tile_size = tile_size
        self.map = [[EmptyLot((0,0)),EmptyLot((0,1)),EmptyLot((0,2)),EmptyLot((0,3)),EmptyLot((0,4))],
                    [EmptyLot((1,0)),EmptyLot((1,1)),EmptyLot((1,2)),EmptyLot((1,3)),EmptyLot((1,4))],
                    [EmptyLot((2,0)),EmptyLot((2,1)),EmptyLot((2,2)),EmptyLot((2,3)),EmptyLot((2,4))]]

        options = []
        for x in range(5):
            for y in range(3):
                options.append((x,y))

        # Add a random dining hall
        dh = random.choice(options)
        options.remove(dh)
        self.map[dh[1]][dh[0]] = DiningHall()
        global_vars.university.buildings.append(self.map[dh[1]][dh[0]])
        self.map[dh[1]][dh[0]].activate()

        # Add a random student housimg
        sh = random.choice(options)
        options.remove(sh)
        self.map[sh[1]][sh[0]] = StudentHousing()
        global_vars.university.buildings.append(self.map[sh[1]][sh[0]])
        self.map[sh[1]][sh[0]].activate()

        # Add a random lecture hall
        lh = random.choice(options)
        options.remove(lh)
        self.map[lh[1]][lh[0]] = LectureHall()
        global_vars.university.buildings.append(self.map[lh[1]][lh[0]])


        # Add a random library
        l = random.choice(options)
        options.remove(l)
        self.map[l[1]][l[0]] = Library()
        global_vars.university.buildings.append(self.map[l[1]][l[0]])


        self.surface = self.get_surface()


    def try_click(self, pos):
        for rect in self.rects:
            if rect[0].collidepoint(pos):
                return rect[1]

        return None

    def construct_building(self, pos, building):
        con = Construction(building.constructionTime, pos, building.name)
        con.future = building
        con.pos = pos
        self.map[pos[0]][pos[1]] = con
        self.constructions.append(con)
        self.surface = self.get_surface()

    def replace_lot(self, lot, building):
        con = Construction(building.constructionTime, lot.pos, building.name)
        con.future = building
        con.pos = lot.pos
        lot = con
        self.constructions.append(con)
        self.surface = self.get_surface()

    def update_construction(self):
        for con in self.constructions:
            con.counter -= 1
            con.effects = [con.name + " will be",
                            "completed in ",
                           str(con.counter) + " months."]
            if con.counter == 0:
                self.map[con.pos[0]][con.pos[1]] = con.future
                global_vars.university.buildings.append(con.future)
                con.future.activate()
                self.surface = self.get_surface()

    def get_surface(self):
        tile_size = self.tile_size
        pygame = self.pygame
        self.rects.clear()

        map_surface = pygame.Surface((68*tile_size, 42*tile_size))

        # Draw the sidewalks
        street_horiz = Sprite('Resources/street_horizontal', (0,0), (10,3))
        street_vert = Sprite('Resources/street_vertical', (0,0), (3,10))
        street_hub = Sprite('Resources/street_hub', (0,0), (3,3))

        # Draw the horizontal streets
        y = 0
        for row in range(4):
            x = 3*tile_size
            for col in range(5):
                map_surface.blit(street_horiz.surface, (x,y))

                x+=13*tile_size
            y+=13*tile_size

        # Draw the vertical streets
        y = 3*tile_size
        for row in range(3):
            x=0
            for col in range(6):
                map_surface.blit(street_vert.surface, (x,y))
                x+=13*tile_size
            y+=13*tile_size

        # Draw the hubs
        y = 0
        for row in range(4):
            x=0
            for col in range(6):
                map_surface.blit(street_hub.surface, (x,y))
                x+=13*tile_size
            y+=13*tile_size

        # Draw grid of sprites
        y = 3*tile_size
        for row in self.map:
            x = 3*tile_size
            for building in row:
                # Draw the building
                map_surface.blit(building.sprite.surface, (x,y))
                self.rects.append((Rect(x, y, 10 * tile_size, 10 * tile_size), building))
                # Move x, leaving room from the road between the buidlings
                x += 13*tile_size
            y += 13*tile_size

        return map_surface

    def getList():
        list = []
        list.append(DiningHall())
        list.append(LectureHall())
        list.append(Library())
        list.append(ResearchLab())
        list.append(Stadium())
        list.append(StudentHousing())
        list.append(StudentUnion())

        return list
