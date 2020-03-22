import os

import pygame
from pygame.surface import Surface

from Engine.game.controllers import ObjectsController


class Window:

    def __init__(self, width, height, centered=False):
        if centered:
            self.center()

        self.win: Surface = pygame.display.set_mode((width, height))

    @classmethod
    def center(cls):
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    def draw(self, obj: Surface, position=(0, 0)):
        self.win.blit(obj, position)

    def update(self):
        self.draw_game_objects()
        pygame.display.update()

    def draw_game_objects(self):
        for game_objects in ObjectsController.observers:
            game_objects.draw(self.win)
