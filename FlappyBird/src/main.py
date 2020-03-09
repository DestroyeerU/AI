from Engine import GameObject, Slider
from Engine.game.window import Window
from Engine.utils.image_processing import load_image_scaled

WINDOW_WIDTH = 520
WINDOW_HEIGHT = 720

BASE_HEIGHT = 112
BASE_Y = WINDOW_HEIGHT - BASE_HEIGHT


BASE_IMG = load_image_scaled('../imgs/base.png', (WINDOW_WIDTH, BASE_HEIGHT))
BACKGROUND_IMG = load_image_scaled('../imgs/background.png', (WINDOW_WIDTH, WINDOW_HEIGHT))


def init_components():
    background = GameObject(image=BACKGROUND_IMG)

    base_objects = [GameObject(y=BASE_Y, image=BASE_IMG) for _ in range(10)]
    base = Slider(-4, base_objects)


def main():
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, centered=True, fps=60)

    init_components()

    window.start()


if __name__ == '__main__':
    main()
