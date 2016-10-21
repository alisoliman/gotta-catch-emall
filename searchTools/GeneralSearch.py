from objects import Node
from objects.Enums import Search


class GeneralSearch():
    def __init__(self, problem, quingFunction):
        self.problem = problem
        self.quingFunction = quingFunction
        self.visited_nodes = ()

    def breadth_first_search(self, nodes, node):
        available_ops = self.problem.operators(node.state)
        expanded_nodes = node.apply_operator(self.problem, node, available_ops)
        for i in range(0, len(expanded_nodes)):
            if expanded_nodes[i] not in self.visited_nodes:
                self.visited_nodes.add(expanded_nodes[i])
                nodes.append(expanded_nodes[i])
        return nodes
        # if problem.goal_test(node.state):
        #     return node
        # queue = FIFOQueue()
        # queue.append(node)
        # visited_nodes = set()
        # while queue:
        #     node = queue.pop()
        #     visited_nodes.add(node.state)
        #     for child in node.expand(problem):
        #         if child.state not in visited_nodes and child not in queue:
        #             if problem.goal_test(child.state):
        #                 return child
        #             queue.append(child)
        # return None

    def depth_first_search(self,problem):
        pass

    def iterative_deepening_search(self,problem):
        pass

    def uniform_cost_search(self,problem):
        pass

    def search(self):
        nodes = Node(self.problem.initial)

        while True:
            if nodes.empty():
                return "Failure";
            node = nodes.get()
            if self.problem.goal_test(node.state):
                return node
            nodes = self.adjust_queue(nodes, node, self.quingFunction)

    def adjust_queue(self, nodes, node, quingFunction):
        if quingFunction == Search.BF:
            self.breadth_first_search(nodes, node)
        elif quingFunction == Search.DF:
            self.depth_first_search()
        elif quingFunction == Search.ID:
            self.iterative_deepening_search()
        elif quingFunction == Search.UC:
            self.uniform_cost_search()