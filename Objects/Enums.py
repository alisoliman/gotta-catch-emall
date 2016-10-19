from enum import Enum


class Operator(Enum):
    forward = 1
    rotateLeft = 2
    rotateRight = 3


class Orientation(Enum):
    west = 1
    east = 2
    north = 3
    south = 4


class Search():
    BF = 1
    DF = 2
    ID = 3
    UC = 4
