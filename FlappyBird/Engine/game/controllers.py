from Engine.models.base import GameObject


class ObjectsController:
    game_objects = []

    @staticmethod
    def add(game_object: GameObject):
        ObjectsController.game_objects.append(game_object)

    @staticmethod
    def remove(game_object: GameObject):
        ObjectsController.game_objects.remove(game_object)
