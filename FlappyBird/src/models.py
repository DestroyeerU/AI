import pygame

from Engine import GameObject, Animation
from Engine.physics.motion import ConstantAccelerationMotion
from Engine.utils.image_processing import load_images_in_dir


class Bird(GameObject):

    def __init__(self, images_path, jump_force, acceleration, max_rotation, max_displacement, **kwargs):
        super().__init__(**kwargs)

        images = load_images_in_dir(images_path)
        images_order = [0, 1, 2, 1, 0]

        self.animation = Animation(images, images_order)

        self.max_rotation = max_rotation

        self.jump_force = jump_force
        self.motion = ConstantAccelerationMotion(transform=self.transform, acceleration=acceleration, max_displacement=max_displacement)

    def update(self):
        self.motion.update()

        # if displacement < 0 or self.y < self.height + 50:
        #     if self.rotation < self.MAX_ROTATION:
        #         self.rotation = self.MAX_ROTATION
        # else:
        #     if self.rotation > -90:
        #         self.rotation -= self.ROTATION_VELOCITY
        #

    def jump(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.motion.move_time = 1
            self.motion.speed = -6

            # create add force on physics
