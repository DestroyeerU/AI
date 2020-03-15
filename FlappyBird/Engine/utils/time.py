import time

import pygame


class Time:
    delta_time = 0

    @staticmethod
    def set_delta_time(millis: int):
        Time.delta_time = millis / 1000

    # @staticmethod
    # def get_millis(precision: int = 0) -> int:
    #     current_time = int(round(time.time() * 1000))
    #     return current_time - Time.init_time

    # @staticmethod
    # def get_delta_time() -> float:
    #     current_time = Time.get_millis()
    #     delta_time = (current_time - Time.last_time)
    #
    #     Time.last_time = current_time
    #     return delta_time
