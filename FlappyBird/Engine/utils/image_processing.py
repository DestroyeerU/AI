import os
from typing import Optional

import pygame
from pygame.surface import Surface
from pygame.transform import scale2x


def is_image_file(filename) -> bool:
    images_extension = ['.png']
    file_extension = os.path.splitext(filename)[1]

    return file_extension in images_extension


def load_image(path) -> Surface:
    if is_image_file(path):
        return pygame.image.load(path)


def load_images_in_dir(dir_path) -> [Surface]:
    images = []

    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        image = load_image(file_path)

        images.append(image)

    return images


def load_image_scaled(path, scale) -> Surface:
    image = load_image(path)
    return pygame.transform.scale(image, scale)


def load_images_scaled(dir_path, scale) -> [Surface]:
    images_scaled = []

    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        image = load_image_scaled(file_path, scale)

        images_scaled.append(image)

    return images_scaled
