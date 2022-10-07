import pygame
import player
from map import CAMERA_POSITION


class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100, 300)

        # center camera w, h
        # self.half_w = self.display_surface.get_size()[0] // 2
        # self.half_h = self.display_surface.get_size()[1] // 2

        # camera offset half
        cam_left = CAMERA_POSITION['left']
        cam_top = CAMERA_POSITION['top']
        cam_width = self.display_surface.get_size()[0] - (cam_left + CAMERA_POSITION['right'])
        cam_height = self.display_surface.get_size()[1] - (cam_top + CAMERA_POSITION['bottom'])

        self.camera_rect = pygame.Rect(cam_left, cam_top, cam_width, cam_height)

    def custom_draw(self, player):

        # offset camera player
        # self.offset.x = player.rect.centerx - self.half_w
        # self.offset.y = player.rect.centery - self.half_h

        # getting the cam pos
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom


        # camera offset
        self.offset = pygame.math.Vector2(self.camera_rect.left - CAMERA_POSITION['left'],
                                          self.camera_rect.top - CAMERA_POSITION['top'])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
