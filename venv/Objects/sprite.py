import program
import pickle

class Sprite:
    def __init__(self, data_url, pos, size):
        self.data_url = data_url
        self.size = size
        self.pos = pos

        # Get some global variables from Program
        pygame = program.pygame
        tileset = program.tileset
        tile_size = program.tile_size
        tile_scale = program.tile_scale

        # Create a blank surface to draw sprite on
        self.surface = pygame.Surface((tileset.tile_size*tile_scale*size[0], tileset.tile_size*tile_scale*size[1]))

        # Read tile data from file
        with open(data_url) as f:
            self.tile_matrix = pickle.loads(eval(f.read()))

        # Use tile data to draw tiles onto surface
        for y in range(size[1]):
            for x in range(size[0]):
                # Read tile data
                cell = self.tile_matrix[x][y]
                # Grab tile from tileset and scale it
                tile_scaled = pygame.transform.scale(tileset.get_tile(cell), (int(tile_size*tile_scale), int(tile_size*tile_scale)))
                # Scale and draw the tile onto the appropriate area on the surface
                self.surface.blit(tile_scaled, (x*tile_size*tile_scale, y*tile_size*tile_scale))
