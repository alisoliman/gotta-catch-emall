from objects.Operator import Operator
from objects.Orientation import Orientation

from objects import State
from objects.Maze import Maze
from searchTools.SearchProblem import SearchProblem


class CatchEmProblem(SearchProblem):
    def __init__(self):
        self.available_operators = [Operator.forward, Operator.rotateLeft, Operator.rotateRight]
        self.startCell = Maze.cells[Maze.startLocation.x, Maze.startLocation.y]
        self.initialState = State.State(startCell, Orientation.Orientation.forward, 0)

    def operators(self, state):
        pass

    def main(self):
        pass
