from objects.Operator import Operator
from objects.Orientation import Orientation

from objects import State
from objects.Maze import Maze

class CatchEmProblem():
    def __init__(self):
        operators = [Operator.Operator.forward, Operator.Operator.rotateLeft, Operator.Operator.rotateRight]
        startCell = Maze.cells[Maze.startLocation.x, Maze.startLocation.y]
        initialState = State.State(startCell, Orientation.Orientation.forward, 0)


    def main(self):
        pass
