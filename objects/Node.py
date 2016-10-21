from objects import Location
from objects.Enums import Orientation, Operator


class Node():
    def __init__(self, state, parent=None, op=None, depth = 0, pathCost=0):
        self.state = state
        self.parent = parent
        self.operation = op
        self.depth = depth
        if parent:
            self.depth = parent.depth + 1
        self.pathCost = pathCost


    def apply_operator(self, problem, node, operators):

        for i in range(0, len(operators)):
            if operators[i] == Operator.forward:
                new_loc = self.move_forward(node.state.cell.location, node.state.orientation)
                new_orientation = State.orientation
                new_cell = problem.maze.cells[new_loc.x][new_loc.y]
                time_to_hatch = node.state.time_left_to_hatch -1 ;
                if new_cell.has_pokemon:
                    num_pokes
                else:


            elif operators[i] == Operator.rotateLeft:


            elif operators[i] == Operator.rotateRight:



    def move_forward(self, location, orientation):
        if orientation == Orientation.east:
            return Location.Location(location.x + 1, location.y)

        elif orientation == Orientation.west:
            return Location.Location(location.x - 1, location.y)

        elif orientation == Orientation.south:
            return Location.Location(location.x, location.y - 1)

        elif orientation == Orientation.north:
            return Location.Location(location.x, location.y + 1)
