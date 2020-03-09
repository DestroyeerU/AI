import os

import pygame
from pygame.surface import Surface
from pygame.time import Clock

from Engine.game.controllers import ObjectsController


class View:

    def __init__(self, fps: int = 60):
        self.fps = fps
        self.clock = pygame.time.Clock()

        self.running = False

    def start(self):
        self.running = True
        self.__run__()

    def stop(self):
        self.running = False

    def __run__(self):
        while self.running:
            self.clock.tick(self.fps)
            self.check_default_events()
            self.update()

    def update(self):
        pass

    @classmethod
    def check_default_events(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cls.end_game()

    @classmethod
    def end_game(cls):
        pygame.quit()
        quit()


class Window(View):

    def __init__(self, width, height, centered=False, **kwargs):
        super().__init__(**kwargs)

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
        for game_objects in ObjectsController.game_objects:
            game_objects.draw(self.win)
