from objects.Operator import Operator
from objects.Orientation import Orientation

from objects import State
from objects.Maze import Maze
from searchTools.SearchProblem import SearchProblem


class CatchEmProblem(SearchProblem):
    def __init__(self):
        self.operators = [Operator.forward, Operator.rotateLeft, Operator.rotateRight]
        self.startCell = Maze.cells[Maze.startLocation.x, Maze.startLocation.y]
        self.initialState = State.State(self.startCell, Orientation.Orientation.forward, 0)


    def operators(self, state):
        available_operators = []
        if((state.orientation == Orientation.north and state.cell.north == False) or
                (state.orientation == Orientation.east and state.cell.east == False) or
                (state.orientation == Orientation.south and state.cell.south == False) or
                (state.orientation == Orientation.west and state.cell.west == False)):
                    available_operators.append(self.operators[0])

        if ((state.orientation == Orientation.north and state.cell.west == False) or
                (state.orientation == Orientation.west and state.cell.south == False) or
                (state.orientation == Orientation.south and state.cell.east== False) or
                (state.orientation == Orientation.east and state.cell.north == False)):
                    available_operators.append(self.operators[1])

        if((state.orientation == Orientation.north and state.cell.east == False) or
               (state.orientation == Orientation.east and state.cell.south == False) or
               (state.orientation == Orientation.south and state.cell.west == False) or
               (state.orientation == Orientation.west and state.cell.north == False)):
            available_operators.append(self.operators[2])

        return available_operators

    def goal_test(self, state):
        if(state.num_pokemons == Maze.total_pokemons and state.time_left_to_hatch == 0 and state.cell.location == Maze.endLocation):
            return True
        else:
            return False


    def path_cost(self, c, state1, action, state2):
        return c + 1



