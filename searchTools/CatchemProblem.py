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
        self.visited_states = []
        # print(self.initialState)


    def get_operators(self, state):
        available_operators = []

        # if ((state.orientation == Orientation.north and state.cell.north and state.cell.east and state.cell.west) or
        #     (state.orientation == Orientation.east and state.cell.south and state.cell.north and state.cell.east) or
        #     (state.orientation == Orientation.south and state.cell.south and state.cell.west and state.cell.east) or
        #     (state.orientation == Orientation.west and state.cell.south and state.cell.west and state.cell.north)):
        #     available_operators.append(self.operators[1])
        # else:
        if ((state.orientation == Orientation.north and not state.cell.north) or
            (state.orientation == Orientation.east and state.cell.east == False) or
            (state.orientation == Orientation.south and state.cell.south == False) or
                (state.orientation == Orientation.west and state.cell.west == False)):
            available_operators.append(self.operators[0])
        available_operators.append(self.operators[1])
        available_operators.append(self.operators[2])
        print "available_operators", available_operators
        return available_operators

    def goal_test(self, state):
        # print "It checked the goal state"
        if(state.num_pokemons >= self.maze.total_pokemons and state.time_left_to_hatch <= 0 and state.cell.location.x == self.maze.endLocation.x
           and state.cell.location.y == self.maze.endLocation.y):
            print(":DDDDDDDDDDD")
            print ("SUCCESS!")
            return True
        else:
            print(":(((((((((((((((((((")
            return False


    def path_cost(self, c, state1, action, state2):
        return c + 1

    def check_visited_states(self, new_state):
        for i in range(0, len(self.visited_states)):
            if (new_state.cell.location.x == self.visited_states[i].cell.location.x and
                        new_state.cell.location.y == self.visited_states[i].cell.location.y and
                        new_state.cell.has_pokemon == self.visited_states[i].cell.has_pokemon and
                        new_state.orientation == self.visited_states[i].orientation and
                        new_state.num_pokemons == self.visited_states[i].num_pokemons and
                        new_state.time_left_to_hatch == self.visited_states[i].time_left_to_hatch):
                return True
            else:
                continue
        return False





