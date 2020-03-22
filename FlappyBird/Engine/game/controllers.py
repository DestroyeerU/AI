from Engine.models.base import GameObject


class Observer:
    observers = []

    @staticmethod
    def add(game_object: GameObject):
        Observer.observers.append(game_object)

    @staticmethod
    def remove(game_object: GameObject):
        Observer.observers.remove(game_object)


class ObjectsController(Observer):
    pass
