from additional_packages.utils import FIFOQueue
from Objects import Node

class GeneralSearch():

    def __init__(problem, quingFunction):
        pass

    @property
    def breadth_first_search(problem):
        node = Node(problem.initial)
        if problem.goal_test(node.state):
            return node
        queue = FIFOQueue()
        queue.append(node)
        explored = set()
        while queue:
            node = queue.pop()
            explored.add(node.state)
            for child in node.expand(problem):
                if child.state not in explored and child not in queue:
                    if problem.goal_test(child.state):
                        return child
                    queue.append(child)
        return None




