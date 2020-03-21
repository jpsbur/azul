import enum


class Tile(enum.Enum):
    FIRST_MOVE = 0
    BLACK = 1
    BLUE = 2
    ORANGE = 3
    RED = 4
    WHITE = 5


class InvalidMoveError(Exception):
    pass
