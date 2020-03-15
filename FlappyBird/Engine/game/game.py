import pygame

from Engine.game.window import Window
from Engine.utils import Time
from Engine.utils.input import Input


class Game:
    FPS = 60

    def __init__(self, fps: int = 60):
        self.FPS = fps
        self.clock = pygame.time.Clock()

        self.running = False
        self.window: Window = Window(0, 0)

        Input.add(self.end_game)

    def create_window(self, width: int, height: int, centered=False):
        self.window = Window(width, height, centered)

    def start(self):
        self.running = True
        self.__run__()

    def stop(self):
        self.running = False

    def __run__(self):
        while self.running:
            self.window.update()

            delta_time = self.clock.tick(self.FPS)
            Time.set_delta_time(delta_time)

            Input.check_events()

    @staticmethod
    def end_game(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
