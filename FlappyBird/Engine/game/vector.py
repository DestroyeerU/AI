class Vector2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def zero():
        return Vector2(0, 0)
