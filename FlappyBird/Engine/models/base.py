import pygame
from pygame.surface import Surface

import Engine


class Transform:

    def __init__(self, x, y, width, height, rotation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation

    def rotate(self, img, rotation):
        self.rotation = rotation
        image_center = img.get_rect(topleft=(self.x, self.y)).center

        rotated_image = pygame.transform.rotate(img, rotation)
        new_rect = rotated_image.get_rect(center=image_center)

        return rotated_image, new_rect


class GameObject:

    def __init__(self, x=0, y=0, rotation=0, image: Surface = None):
        self.current_image: Surface = image

        width = 0 if not image else image.get_width()
        height = 0 if not image else image.get_height()

        self.transform = Transform(x, y, width, height, rotation)

        Engine.game.controllers.ObjectsController.add(self)

    def draw(self, win: Surface):
        win.blit(self.current_image, (self.transform.x, self.transform.y))

    def destroy(self):
        Engine.game.controllers.ObjectsController.remove(self)


class Animation:

    def __init__(self, images=None, display_order=None):
        self.images = images or []
        self.display_order = display_order or []

