import contextlib

import pygame
from pygame.surface import Surface

from Engine import game
from Engine.game.transform import Transform


class Animation:

    def __init__(self, images, display_order, next_animation_times=None, next_animation_fixed_time=0.1):
        self.images: list[Surface] = images or []
        self.display_order: list[int] = display_order or []
        self.animation_times: list[int] = next_animation_times or [next_animation_fixed_time for _ in range(len(self.display_order))]

        self.current_time = 0
        self.current_display_index = 0

    def get_current_animation_image(self) -> Surface:
        self.current_time += 1 / game.game.Game.FPS

        if self.current_time >= self.animation_times[self.current_display_index]:
            self.__next_image__()

        image_index = self.display_order[self.current_display_index]
        return self.images[image_index]

    def __next_image__(self) -> None:
        self.current_time = 0
        self.current_display_index += 1

        if self.current_display_index == len(self.images):
            self.current_display_index = 0


class GameObject:

    def __init__(self, x=0, y=0, rotation=0, image: Surface = None, animation: Animation = None):
        self.current_image: Surface = image

        self.animation = animation

        width = 0 if not image else image.get_width()
        height = 0 if not image else image.get_height()

        self.transform = Transform(x, y, width, height, rotation)

        game.controllers.ObjectsController.add(self)

    def draw(self, win: Surface):
        self.update()
        self.__update__()
        self.late_update()

        with contextlib.suppress(TypeError):    # if self.current_image:
            win.blit(self.current_image, (self.transform.x, self.transform.y))

    def __update__(self):
        if self.animation:
            self.current_image = self.animation.get_current_animation_image()

    def update(self):
        pass

    def late_update(self):
        pass

    def destroy(self):
        game.controllers.ObjectsController.remove(self)
        Input.remove(self)
