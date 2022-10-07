import pygame, sys
from map import *
from level import Level


pygame.init()
screem = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Map Level')
clock = pygame.time.Clock()

level = Level()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screem.fill(BG_COLOR)
    level.run()


    pygame.display.update()
    clock.tick(60)


