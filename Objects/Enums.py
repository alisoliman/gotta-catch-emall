from enum import Enum


class Operator(Enum):
    forward = 1
    rotateLeft = 2
    rotateRight = 3


class Orientation(Enum):
    north = 1
    east = 2
    south = 3
    west = 4


class Search():
    BF = 1
    DF = 2
    ID = 3
    UC = 4
