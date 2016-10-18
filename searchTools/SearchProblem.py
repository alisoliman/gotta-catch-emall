from objects.Orientation import Orientation
from objects import State
from objects.Maze import Maze
from objects import Operator
from additional_packages.utils import is_in

class SearchProblem:
    def __init__(self, operators, initState, goal, pathCostFunction):
        self.operators = operators
        self.initialState = initState
        self.goal = goal
        self.pathCostFunction = pathCostFunction

    def operators(self, state):
        raise NotImplementedError

    def goal_test(self, state):
        raise NotImplementedError

    def path_cost(self, c, state1, action, state2):
        raise NotImplementedError

    def main(self):
        pass
