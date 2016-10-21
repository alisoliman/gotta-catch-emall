from objects import Location
from objects.Enums import Orientation, Operator
from objects.State import State


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
        nodes = []
        for i in range(0, len(operators)):
            if operators[i] == Operator.forward:
                print "Operator forward detected"
                new_loc = self.move_forward(node.state.cell.location, node.state.orientation)
                new_orientation = node.state.orientation
                new_cell = problem.maze.cells[new_loc.x][new_loc.y]
                time_to_hatch = node.state.time_left_to_hatch -1 ;
                num_pokes = node.state.num_pokemons
                if new_cell.has_pokemon:
                    num_pokes += 1
                new_state = State(new_cell, num_pokes, new_orientation, time_to_hatch)
                new_node = Node(new_state, node, operators[i], node.depth+1)
                nodes.append(new_node)
            elif operators[i] == Operator.rotateLeft:
                print "Operator rotate left detected"
                new_orientation = self.rotateLeft(State.orientation)
                time_to_hatch = node.state.time_left_to_hatch - 1;
                new_state = State.State(node.state.cell, new_orientation, problem.state.num_pokemons, time_to_hatch)
                new_node = Node.Node(new_state, node, operators[i], node.depth+1)
                nodes.append(new_node)
            elif operators[i] == Operator.rotateRight:
                print "Operator rotate right detected"
                new_orientation = self.rotateRight(State.orientation)
                time_to_hatch = node.state.time_left_to_hatch - 1;
                new_state = State.State(node.state.cell, new_orientation, problem.state.num_pokemons, time_to_hatch)
                new_node = Node.Node(new_state, node, operators[i], node.depth + 1)
                nodes.append(new_node)
        return nodes


    def move_forward(self, location, orientation):
        if orientation == Orientation.east:
            return Location.Location(location.x + 1, location.y)

        elif orientation == Orientation.west:
            return Location.Location(location.x - 1, location.y)

        elif orientation == Orientation.south:
            return Location.Location(location.x, location.y - 1)

        elif orientation == Orientation.north:
            return Location.Location(location.x, location.y + 1)

    def rotateLeft(x):
        return {
            Orientation.east: Orientation.north,
            Orientation.north: Orientation.west,
            Orientation.west: Orientation.south,
            Orientation.south: Orientation.east
        }[x]

    def rotateRight(x):
        return {
            Orientation.east: Orientation.south,
            Orientation.south: Orientation.west,
            Orientation.west: Orientation.north,
            Orientation.north: Orientation.east
        }[x]

    def __str__(self):
        return "state: {} parent: {}, depth: {}".format(self.state, self.parent, self.depth)
