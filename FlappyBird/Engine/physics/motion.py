import pygame

from Engine import Transform
from Engine.utils.time import Time


class Physic:

    def __init__(self, mass: float = 1, initial_speed: float = 0):
        self.mass = mass
        self.speed = initial_speed

    def add_force(self, force: float, time: float) -> None:
        pass


'''
I = F * t
I = Qf - Qi

Q = m * v

F * t = m * v

v = (F * t) / m

d = v * t

'''


class Motion(Physic):

    def __init__(self, transform: Transform, acceleration: float, max_displacement: float = None, **kwargs):
        super().__init__(**kwargs)

        self.transform = transform

        self.acceleration = acceleration

        self.max_displacement = max_displacement

        self.displacement = 0.0
        self.move_time = 0

    def update(self) -> None:
        self.move_time += Time.delta_time

        self.calculate_displacement()
        self.calculate_speed()

        self.transform.y += self.displacement

    def calculate_speed(self) -> None:
        self.speed += self.acceleration * Time.delta_time

    def calculate_displacement(self) -> None:
        pass


class ConstantAccelerationMotion(Motion):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_displacement(self) -> None:
        self.displacement = self.speed * self.move_time + (self.acceleration * self.move_time ** 2) / 2.0

        if self.displacement >= self.max_displacement:
            self.displacement = self.max_displacement
