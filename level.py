import pygame
from map import *
from player import Player
from tile import Tile
from camera import Camera


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = Camera()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_level()

    # coordinates of fields and nearby on the map
    def setup_level(self):
        for row_index, row in enumerate(LEVEL_MAP):
            for col_index, column in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if column == 'X':
                    Tile((x, y), [self.visible_sprites, self.collision_sprites])
                if column == 'P':
                    self.player = Player((x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)

    def run(self):
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)


# class Camera(pygame.sprite.Group):
#     def __init__(self):
#         super().__init__()
#         self.display_surface = pygame.display.get_surface()
#         self.offset = pygame.math.Vector2(100, 300)
#
#     def custom_draw(self):
#         for sprite in self.sprites():
#             offset_pos = sprite.rect.topleft + self.offset
#             self.display_surface.blit(sprite.image, offset_pos)
