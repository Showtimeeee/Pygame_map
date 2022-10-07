import pygame
from map import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=pos)

        # movement player
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.gravity = 1
        self.jump_speed = 18
        self.collision_sprites = collision_sprites
        self.jump_on_floor = False

    def fly(self):
        keys = pygame.key.get_pressed()

    # keyboard WASD
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # jump
        if keys[pygame.K_SPACE] and self.jump_on_floor:
            self.direction.y = -self.jump_speed

    # collision player to tiles
    def horizont_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertic_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.jump_on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        # one jump
        if self.jump_on_floor and self.direction.y != 0:
            self.jump_on_floor = False

    def app_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizont_collisions()
        self.app_gravity()
        self.vertic_collisions()

