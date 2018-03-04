class Tileset:
    def __init__(self, pygame, img_url, width, height):
        self.img_url = img_url
        self.width = width
        self.height = height
        self.pygame = pygame
        self.image = self.pygame.image.load(img_url)
        self.tile_size = self.image.get_size()[0]/width
        self.tile_matrix = []
        for x in range(self.width):
            self.tile_matrix.append([])
            for y in range(self.height):
                self.tile_matrix[x].append((0,0))
        for y in range(self.height):
            for x in range(self.width):
                self.tile_matrix[x][y] = pygame.Surface((self.tile_size, self.tile_size))
                self.tile_matrix[x][y].blit(self.image, (0,0), (x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size))

    def get_tile(self, tile_coord):
        return self.tile_matrix[tile_coord[0]][tile_coord[1]]
