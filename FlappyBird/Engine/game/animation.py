from pygame.surface import Surface


class Animation:

    def __init__(self, images, display_order, next_animation_times=None, next_animation_fixed_time=0.1):
        self.images: list[Surface] = images or []
        self.display_order: list[int] = display_order or []
        self.animation_times: list[int] = next_animation_times or [next_animation_fixed_time for _ in range(len(self.display_order))]

        self.current_time = 0
        self.current_display_index = 0

    def get_current_animation_image(self) -> Surface:
        self.current_time += 1 / Game.FPS

        if self.current_time >= self.animation_times[self.current_display_index]:
            self.__next_image__()

        image_index = self.display_order[self.current_display_index]
        return self.images[image_index]

    def __next_image__(self) -> None:
        self.current_time = 0
        self.current_display_index += 1

        if self.current_display_index == len(self.images):
            self.current_display_index = 0
