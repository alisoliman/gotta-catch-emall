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
        first_state = problem.initialState
        new_state = State(problem.initialState.cell, Orientation.north, 0, problem.initialState.time_left_to_hatch)

        for i in range(0, len(operators)):
            if operators[i] == Operator.forward:
                print "Operator forward detected"
                new_loc = self.move_forward(node.state.cell.location, node.state.orientation)
                new_orientation = node.state.orientation
                new_cell = problem.maze.cells[new_loc.x][new_loc.y]
                if node.state.time_left_to_hatch > 0:
                    time_to_hatch = node.state.time_left_to_hatch -1 ;
                else:
                    time_to_hatch = 0
                num_pokes = node.state.num_pokemons
                if new_cell.has_pokemon:
                    num_pokes += 1
                    new_cell.has_pokemon = False
                new_state = State(new_cell, new_orientation, num_pokes, time_to_hatch)
                print "CHECK THIS OUT##########"
                print problem.check_visited_states(new_state)
                print len(problem.visited_states)
                if problem.check_visited_states(new_state):
                    continue
                else:
                    problem.visited_states.append(new_state)
                    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                    print len(problem.visited_states)
                    new_node = Node(new_state, node, operators[i], node.depth+1, node.pathCost+2)
                    nodes.append(new_node)
            elif operators[i] == Operator.rotateLeft:
                print "Operator rotate left detected"
                new_orientation = self.rotateLeft(node.state.orientation)
                if node.state.time_left_to_hatch > 0:
                    time_to_hatch = node.state.time_left_to_hatch - 1;
                else:
                    time_to_hatch = 0
                new_state = State(node.state.cell, new_orientation, node.state.num_pokemons, time_to_hatch)
                if problem.check_visited_states(new_state):
                    continue
                else:
                    problem.visited_states.append(new_state)
                    new_node = Node(new_state, node, operators[i], node.depth+1, node.pathCost+1)
                    nodes.append(new_node)
            elif operators[i] == Operator.rotateRight:
                print "Operator rotate right detected"
                new_orientation = self.rotateRight(node.state.orientation)
                if node.state.time_left_to_hatch > 0:
                    time_to_hatch = node.state.time_left_to_hatch - 1;
                else:
                    time_to_hatch = 0
                new_state = State(node.state.cell, new_orientation, node.state.num_pokemons, time_to_hatch)
                if problem.check_visited_states(new_state):
                    continue
                else:
                    problem.visited_states.append(new_state)
                    new_node = Node(new_state, node, operators[i], node.depth + 1, node.pathCost+1)
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

    def rotateLeft(self, x):
        return {
            Orientation.east: Orientation.north,
            Orientation.north: Orientation.west,
            Orientation.west: Orientation.south,
            Orientation.south: Orientation.east
        }[x]

    def rotateRight(self, x):
        return {
            Orientation.east: Orientation.south,
            Orientation.south: Orientation.west,
            Orientation.west: Orientation.north,
            Orientation.north: Orientation.east
        }[x]




    def check_visited_states2(self, first_state, new_state):
        if (new_state.cell.location.x == first_state.cell.location.x and
                        new_state.cell.location.y == first_state.cell.location.y and
                        new_state.cell.has_pokemon == first_state.cell.has_pokemon and
                        new_state.orientation == first_state.orientation and
                        new_state.num_pokemons == first_state.num_pokemons and
                        new_state.time_left_to_hatch == first_state.time_left_to_hatch):
                        return True
        else:
            return False

    def __str__(self):
        return "state: {} , depth: {}".format(self.state, self.depth)
