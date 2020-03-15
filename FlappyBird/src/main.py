from Engine import GameObject, Slider
from Engine.game.game import Game
from Engine.utils.image_processing import load_image_scaled
from src.models import Bird

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 690

BASE_HEIGHT = 112
BASE_Y = WINDOW_HEIGHT - BASE_HEIGHT


MAX_PIPE_GAP = int(WINDOW_HEIGHT / 10)

PIPE_WIDTH = 52
PIPE_HEIGHT = 320 + MAX_PIPE_GAP  # default + how long need to be

#                                        birdHeight
BIRD_Y = WINDOW_HEIGHT / 2 - BASE_HEIGHT - 24 / 2


BASE_IMG = load_image_scaled('../imgs/base.png', (WINDOW_WIDTH, BASE_HEIGHT))
BACKGROUND_IMG = load_image_scaled('../imgs/background.png', (WINDOW_WIDTH, WINDOW_HEIGHT))

TOP_PIPE = load_image_scaled('../imgs/pipe.png', (PIPE_WIDTH, PIPE_HEIGHT), flip_y=True)
BOTTOM_PIPE = load_image_scaled('../imgs/pipe.png', (PIPE_WIDTH, PIPE_HEIGHT))


def init_components():
    background = GameObject(image=BACKGROUND_IMG)

    top_pipe = GameObject(image=TOP_PIPE)
    # top_pipe.transform.y = 100

    bottom_pipe = GameObject(image=BOTTOM_PIPE)
    bottom_pipe.transform.y = bottom_pipe.transform.height + MAX_PIPE_GAP

    base_objects = [GameObject(y=BASE_Y, image=BASE_IMG) for _ in range(10)]
    base = Slider(-4, base_objects)


def main():
    from Engine.utils.input import Input

    game = Game(fps=60)
    game.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, centered=True)

    init_components()

    bird = Bird(
        images_path='../imgs/bird',
        jump_force=5,
        acceleration=4,
        max_rotation=20,
        max_displacement=16,
        x=80,
        y=BIRD_Y,
    )

    Input.add(bird.jump)
    game.start()


if __name__ == '__main__':
    main()
