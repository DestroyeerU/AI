import pygame


class Input:
    __observers = []

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            Input.notify_observers(event)

    @staticmethod
    def notify_observers(command):
        for observer_func in Input.__observers:
            observer_func(command)

    @staticmethod
    def add(observer):
        Input.__observers.append(observer)

    @staticmethod
    def remove(observer):
        Input.__observers.remove(observer)
