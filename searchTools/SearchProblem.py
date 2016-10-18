from objects.Orientation import Orientation
from objects import State
from objects.Maze import Maze
from objects import Operator

class SearchProblem():
    def __init__(self, operators, initState, goalTest, pathCostFunction):
        self.operators = operators
        self.initialState = initState
        self.goalTest = goalTest
        self.pathCostFunction = pathCostFunction

    def operators(self, state):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        raise NotImplementedError


