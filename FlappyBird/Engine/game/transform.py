import pygame
from pygame.surface import Surface


class Transform:

    def __init__(self, x=0, y=0, width=100, height=100, rotation=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation

    def rotate(self, img: Surface, rotation):
        self.rotation = rotation
        image_center = img.get_rect(topleft=(self.x, self.y)).center

        rotated_image = pygame.transform.rotate(img, rotation)
        new_rect = rotated_image.get_rect(center=image_center)

        return rotated_image, new_rect
