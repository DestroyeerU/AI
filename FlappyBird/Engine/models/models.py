from pygame.surface import Surface

from Engine.models.base import GameObject


class Slider(GameObject):

    def __init__(self, speed: float, game_objects: [GameObject], adjust_position=True, **kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.game_objects: list[GameObject] = game_objects

        if adjust_position:
            self.adjust_position()

    def adjust_position(self):
        self.game_objects[0].transform.x = 0

        for i in range(1, len(self.game_objects)):
            current_object = self.game_objects[i]
            object_width = current_object.current_image.get_width()

            current_object.transform.x = self.game_objects[i-1].transform.x + object_width

    def update(self):
        for game_object in self.game_objects:
            game_object.transform.x += self.speed

        self.__update_position__()

    def __update_position__(self):
        for i in range(len(self.game_objects)):
            game_object = self.game_objects[i]
            image_width = game_object.current_image.get_width()

            if game_object.transform.x + image_width < 0:
                game_object.transform.x = self.game_objects[i-1].transform.x + image_width
