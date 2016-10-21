from objects.Enums import Operator
from objects.Enums import Orientation

from objects import State
from objects.Maze import Maze
from searchTools.SearchProblem import SearchProblem


class CatchEmProblem(SearchProblem):
    def __init__(self, maze):
        self.maze = maze;
        self.operators = [Operator.forward, Operator.rotateLeft, Operator.rotateRight]
        self.startCell = self.maze.cells[self.maze.startLocation.x][self.maze.startLocation.y]
        self.initialState = State.State(self.startCell, Orientation.north, 0, maze.time_to_hatch)


    def get_operators(self, state):
        available_operators = []
        if((state.orientation == Orientation.north and not state.cell.north ) or
                (state.orientation == Orientation.east and state.cell.east == False) or
                (state.orientation == Orientation.south and state.cell.south == False) or
                (state.orientation == Orientation.west and state.cell.west == False)):
                    available_operators.append(self.operators[0])

        available_operators.append(self.operators[1:3])

        return available_operators

    def goal_test(self, state):
        print "It checked the goal statep"
        if(state.num_pokemons == self.maze.total_pokemons and state.time_left_to_hatch <= 0 and state.cell.location == self.maze.endLocation):
            return True
        else:
            return False


    def path_cost(self, c, state1, action, state2):
        return c + 1



