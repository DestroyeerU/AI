class Physic:

    def __init__(self, mass: float = 1, initial_speed: float = 0):
        self.mass = mass
        self.speed = initial_speed

    def add_force(self, force: float, time: float) -> None:
        pass
