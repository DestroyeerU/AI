import os

import pygame
from pygame.surface import Surface
from pygame.transform import scale2x


def is_image_file(filename) -> bool:
    images_extension = ['.png']
    file_extension = os.path.splitext(filename)[1]

    return file_extension in images_extension


def flip(image: Surface, x=False, y=False):
    return pygame.transform.flip(image, x, y)


def load_image(path, flip_x=False, flip_y=False) -> Surface:
    if is_image_file(path):
        img = pygame.image.load(path)
        return flip(img, flip_x, flip_y)


def load_images_in_dir(dir_path) -> [Surface]:
    images = []

    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        image = load_image(file_path)

        images.append(image)

    return images


def load_image_scaled(path, scale, flip_x=False, flip_y=False) -> Surface:
    image = load_image(path, flip_x, flip_y)
    return pygame.transform.scale(image, scale)


def load_images_scaled(dir_path, scale) -> [Surface]:
    images_scaled = []

    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        image = load_image_scaled(file_path, scale)

        images_scaled.append(image)

    return images_scaled
