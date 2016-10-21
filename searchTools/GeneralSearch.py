from collections import Set

from additional_packages.utils import FIFOQueue
from objects import Node
from objects.Enums import Search
import Queue

class GeneralSearch():
    def __init__(self, problem, quingFunction):
        self.problem = problem
        self.quingFunction = quingFunction
        self.visited_nodes = set()

    def breadth_first_search(self, node):
        available_operators = self.problem.get_operators(node.state)
        nodes_expansion = node.apply_operator(self.problem,node,available_operators)
        print nodes_expansion.__len__()

        return_queue = FIFOQueue()
        return_queue.append(nodes_expansion)
        if(return_queue.__len__()==0):
            return self.breadth_first_search(node)
        else:
            return return_queue
        # for i in range(0, len(expanded_nodes)):
        # print "Looped to expand nodes ",i
        #     if expanded_nodes[i] not in self.visited_nodes:
        #         self.visited_nodes.add(expanded_nodes[i])





        # available_ops = self.problem.get_operators(node.state)
        # expanded_nodes = node.apply_operator(self.problem, node, available_ops)
        # for i in range(0, len(expanded_nodes)):
        #     print "Looped to expand nodes ",i
        #     if expanded_nodes[i] not in self.visited_nodes:
        #         self.visited_nodes.add(expanded_nodes[i])
        #
        # return expanded_nodes



    def depth_first_search(self,problem):
        pass

    def iterative_deepening_search(self,problem):
        pass

    def uniform_cost_search(self,problem):
        pass

    def search(self):
        nodes = FIFOQueue()
        initial_node = Node.Node(self.problem.initialState, 0, 0)
        nodes.append(initial_node)
        # print nodes.__len__()
        while True:
            print ("once")
            if nodes.__len__() == 0:
                return "Failure";
            node = nodes.pop()
            # print nodes.__len__()
            print "It didn't Fail"
            if self.problem.goal_test(node.state):
                return node
            print "Adjust queue method"
            if (self.adjust_queue(nodes, node, self.quingFunction).__len__() != 0):
                nodes = nodes.append(self.adjust_queue(nodes, node, self.quingFunction))
            print "back"

    def adjust_queue(self, nodes, node, quingFunction):
        if quingFunction == Search.BF:
            "Breadth first calling"
            self.breadth_first_search(node)
        elif quingFunction == Search.DF:
            self.depth_first_search()
        elif quingFunction == Search.ID:
            self.iterative_deepening_search()
        elif quingFunction == Search.UC:
            self.uniform_cost_search()