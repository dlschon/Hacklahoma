from Objects.buildings.emptylot import EmptyLot
from Objects.buildings.lecturehall import LectureHall
from Objects.buildings.library import Library
from Objects.buildings.researchlab import ResearchLab
from Objects.buildings.stadium import Stadium
from Objects.buildings.studenthousing import StudentHousing
from Objects.buildings.studentunion import StudentUnion
from Objects.sprite import Sprite

class Map:

    EMPTY_LOT = 0
    LECTURE_HALL = 1
    LIBRARY = 2
    RESEARCH_LAB = 3
    STADIUM = 4
    STUDENT_HOUSING = 5
    STUDENT_UNION = 6

    def __init__(self, pygame, tile_size):
        self.pygame = pygame
        self.tile_size = tile_size
        self.map = [[EmptyLot(),LectureHall(),Library(),EmptyLot(),EmptyLot()],
                    [EmptyLot(),Stadium(),StudentUnion(),StudentHousing(),EmptyLot()],
                    [EmptyLot(),EmptyLot(),ResearchLab(),LectureHall(),LectureHall()]]


    def get_surface(self):
        tile_size = self.tile_size
        pygame = self.pygame

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
                # Move x, leaving room from the road between the buidlings
                x += 13*tile_size
            y += 13*tile_size

        return map_surface

