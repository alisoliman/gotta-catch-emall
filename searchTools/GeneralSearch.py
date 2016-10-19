from additional_packages.utils import FIFOQueue
from Objects import Node
from Objects.Enums import Search


class GeneralSearch():
    def __init__(self, problem, quingFunction):
        self.problem = problem
        self.quingFunction = quingFunction

    def breadth_first_search(self,problem):
        node = Node(problem.initial)
        if problem.goal_test(node.state):
            return node
        queue = FIFOQueue()
        queue.append(node)
        visited_nodes = set()
        while queue:
            node = queue.pop()
            visited_nodes.add(node.state)
            for child in node.expand(problem):
                if child.state not in visited_nodes and child not in queue:
                    if problem.goal_test(child.state):
                        return child
                    queue.append(child)
        return None

    def depth_first_search(self,problem):
        pass

    def iterative_deepening_search(self,problem):
        pass

    def uniform_cost_search(self,problem):
        pass

    def main(self):
        nodes = Node(self.problem.initial)
        while True:
            if nodes.empty():
                return "Failure";
            node = nodes.get()
            if self.problem.goal_test(node.state):
                return node
            nodes = self.adjust_queue(nodes,self.quingFunction)

    def adjust_queue(self, nodes, quingFunction):
        if quingFunction == Search.BF:
            self.breadth_first_search()
        elif quingFunction == Search.DF:
            self.depth_first_search()
        elif quingFunction == Search.ID:
            self.iterative_deepening_search()
        elif quingFunction == Search.UC:
            self.uniform_cost_search()