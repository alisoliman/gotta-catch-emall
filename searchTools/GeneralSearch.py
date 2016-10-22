from collections import Set

from additional_packages import Stack
from additional_packages.PriorityQueue import PriorityQueue
from objects import Node
from objects.Enums import Search
import Queue

class GeneralSearch():
    def __init__(self, problem, quingFunction, heuristic=None):
        self.problem = problem
        self.quingFunction = quingFunction
        self.visited_nodes = []
        self.initialized = False
        self.heuristic = heuristic

    def search(self):
        print "Search strategy: ", self.quingFunction
        nodes = Queue.Queue()
        initial_node = Node.Node(self.problem.initialState, 0, 0)
        nodes.put(initial_node)
        while True:
            # print ("RA7")
            if nodes.empty():
                print "Failure"
            node = nodes.get()
            print(node)
            # print "It didn't Fail"
            if self.problem.goal_test(node.state):
                result = []
                result.append(node)
                print "path from root"
                print self.actions(node)
                print "depth: ", node.depth
                return node
            # print "Adjust queue method"
            nodes = self.adjust_queue(nodes, node, self.quingFunction, self.heuristic)
            # print "back"

    def actions(self, node):
        if node==None:
            return
        print "{}".format(node)
        print "{}".format(node.parent)


    def adjust_queue(self, nodes, node, quingFunction, heuristic):
        if quingFunction == Search.BF:
            # "Breadth first calling"
            return self.breadth_first_search(nodes, node)
        elif quingFunction == Search.DF:
            return self.depth_first_search(nodes, node)
        elif quingFunction == Search.ID:
            return self.iterative_deepening_search(nodes, node, limit=50)
        elif quingFunction == Search.UC:
            return self.uniform_cost_search(nodes, node)
        elif quingFunction == Search.AS:
            return self.a_star_search(nodes, node, heuristic)
        elif quingFunction == Search.GR:
            return self.greedy_search(nodes, node, heuristic)


    def breadth_first_search(self, nodes, node):
        available_ops = self.problem.get_operators(node.state)
        print "available ops: ", available_ops
        expanded_nodes = node.apply_operator(self.problem, node, available_ops)
        for i in range(0, len(expanded_nodes)):
            # print "Looped to expand nodes ",i
            # if not self.check_visited_nodes(expanded_nodes[i]):
            print "dakhal y-add unvisited node"
            print(expanded_nodes[i])
                # self.visited_nodes.append(expanded_nodes[i])
            nodes.put(expanded_nodes[i])
            # else:
            #     continue
            # nodes.put(expanded_nodes[i])
        return nodes

    def depth_first_search(self, nodes, node):
        stack = Stack()
        jj = 0
        while True:
            print "jj: ", jj
            jj += 1
            if nodes.empty():
                break;
            onenode = nodes.get()
            stack.push(onenode)
        print "magtsh"
        available_ops = self.problem.get_operators(node.state)

        print "got that node: ", node.state
        expanded_nodes = node.apply_operator(self.problem, node, available_ops)
        print(len(expanded_nodes))
        for i in range(0, len(expanded_nodes)):
            # print "Looped to expand nodes ", i
            print "dakhal y-add unvisited node"
            print"expanded nodes: ", expanded_nodes[i]
            stack.push(expanded_nodes[i])
        print "stack length: ", stack.size()
        for i in range(0, stack.size()):
            nodes.put(stack.pop())
        return nodes


    def iterative_deepening_search(self, nodes, node, limit):
        stack = Stack.Stack()
        while True:
            if nodes.empty():
                break;
            stack.push(nodes.get())
        print "magtsh"
        for limit_counter in range(0, limit):
            if node.depth >= limit:
                break;
            available_ops = self.problem.get_operators(node.state)
            print "got that node: ", node.state
            expanded_nodes = node.apply_operator(self.problem, node, available_ops)
            print(len(expanded_nodes))
            for i in range(0, len(expanded_nodes)):
                # print "Looped to expand nodes ", i
                print "dakhal y-add unvisited node"
                print"expanded nodes: ", expanded_nodes[i]
                stack.push(expanded_nodes[i])
        print "stack length: ", stack.size()
        for i in range(0, stack.size()):
                nodes.put(stack.pop())
        return nodes

    def uniform_cost_search(self,nodes, node):
        priority = PriorityQueue()
        while True:
            if nodes.empty():
                break
            popped = nodes.get()
            priority.insert(popped, popped.pathCost)
        available_ops = self.problem.get_operators(node.state)
        print "available ops: ", available_ops
        expanded_nodes = node.apply_operator(self.problem, node, available_ops)
        for i in range(0, len(expanded_nodes)):
            # print "Looped to expand nodes ",i
            # if not self.check_visited_nodes(expanded_nodes[i]):
            print "dakhal y-add unvisited node"
            print(expanded_nodes[i])
            # self.visited_nodes.append(expanded_nodes[i])
            priority.insert(expanded_nodes[i], expanded_nodes[i].pathCost)
            # else:
            #     continue
            # nodes.put(expanded_nodes[i])
        while not priority.is_empty():
            nodes.put(priority.remove())
        return nodes

    def greedy_search(self, nodes, node, heuristic):
        priority = PriorityQueue()
        while True:
            if nodes.empty():
                break
            popped = nodes.get()
            if heuristic == 1:
                key = self.manhattan(popped)
            elif heuristic == 2:
                key = self.manhattan_pokes(popped)
            else:
                key = self.manhattan_pokes_time(popped)
            priority.insert(popped, key)
        available_ops = self.problem.get_operators(node.state)
        print "available ops: ", available_ops
        expanded_nodes = node.apply_operator(self.problem, node, available_ops)
        for i in range(0, len(expanded_nodes)):
            # print "Looped to expand nodes ",i
            # if not self.check_visited_nodes(expanded_nodes[i]):
            print "dakhal y-add unvisited node"
            print(expanded_nodes[i])
            # self.visited_nodes.append(expanded_nodes[i])
            if heuristic == 1:
                key = self.manhattan(expanded_nodes[i])
            elif heuristic == 2:
                key = self.manhattan_pokes(expanded_nodes[i])
            else:
                key = self.manhattan_pokes_time(expanded_nodes[i])
            priority.insert(expanded_nodes[i], key)
            # else:
            #     continue
            # nodes.put(expanded_nodes[i])
        while not priority.is_empty():
            nodes.put(priority.remove())
        return nodes

    def a_star_search(self, nodes, node, heuristic):
        priority = PriorityQueue()
        while True:
            if nodes.empty():
                break
            popped = nodes.get()
            if heuristic == 1:
                key = self.manhattan_star(popped)
            elif heuristic == 2:
                key = self.manhattan_pokes_star(popped)
            else:
                key = self.manhattan_pokes_time_star(popped)
            priority.insert(popped, key)
        available_ops = self.problem.get_operators(node.state)
        print "available ops: ", available_ops
        expanded_nodes = node.apply_operator(self.problem, node, available_ops)
        for i in range(0, len(expanded_nodes)):
            # print "Looped to expand nodes ",i
            # if not self.check_visited_nodes(expanded_nodes[i]):
            print "dakhal y-add unvisited node"
            print(expanded_nodes[i])
            # self.visited_nodes.append(expanded_nodes[i])
            if heuristic == 1:
                key = self.manhattan_star(expanded_nodes[i])
            elif heuristic == 2:
                key = self.manhattan_pokes_star(expanded_nodes[i])
            else:
                key = self.manhattan_pokes_time_star(expanded_nodes[i])
            priority.insert(expanded_nodes[i], key)
            # else:
            #     continue
            # nodes.put(expanded_nodes[i])
        while not priority.is_empty():
            nodes.put(priority.remove())
        return nodes


    def manhattan(self, node):
        x_dist = abs(node.state.cell.location.x - self.problem.maze.endLocation.x)
        y_dist = abs(node.state.cell.location.y - self.problem.maze.endLocation.y)
        return x_dist + y_dist

    def manhattan_pokes(self, node):
        x_dist = abs(node.state.cell.location.x - self.problem.maze.endLocation.x)
        y_dist = abs(node.state.cell.location.y - self.problem.maze.endLocation.y)
        uncollected_pokes = self.problem.maze.total_pokemons - node.state.num_pokemons
        return x_dist + y_dist + uncollected_pokes

    def manhattan_pokes_time(self, node):
        x_dist = abs(node.state.cell.location.x - self.problem.maze.endLocation.x)
        y_dist = abs(node.state.cell.location.y - self.problem.maze.endLocation.y)
        uncollected_pokes = self.problem.maze.total_pokemons - node.state.num_pokemons
        time_left = node.state.time_left_to_hatch
        return x_dist + y_dist + uncollected_pokes + time_left

    def manhattan_star(self, node):
        x_dist = abs(node.state.cell.location.x - self.problem.maze.endLocation.x)
        y_dist = abs(node.state.cell.location.y - self.problem.maze.endLocation.y)
        return x_dist + y_dist + node.pathCost

    def manhattan_pokes_star(self, node):
        x_dist = abs(node.state.cell.location.x - self.problem.maze.endLocation.x)
        y_dist = abs(node.state.cell.location.y - self.problem.maze.endLocation.y)
        uncollected_pokes = self.problem.maze.total_pokemons - node.state.num_pokemons
        return x_dist + y_dist + uncollected_pokes + node.pathCost

    def manhattan_pokes_time_star(self, node):
        x_dist = abs(node.state.cell.location.x - self.problem.maze.endLocation.x)
        y_dist = abs(node.state.cell.location.y - self.problem.maze.endLocation.y)
        uncollected_pokes = self.problem.maze.total_pokemons - node.state.num_pokemons
        time_left = node.state.time_left_to_hatch
        return x_dist + y_dist + uncollected_pokes + time_left + node.pathCost

    def check_visited_nodes(self, ein):
        for i in range(0, len(self.visited_nodes)):
            # print "check this out@@@@@@@@@@"
            # print self.problem.check_visited_states(ein.state)
            if (self.problem.check_visited_states(ein.state) and
                (ein.operation == self.visited_nodes[i].operation) and
                (ein.depth == self.visited_nodes[i].depth) and
                (ein.pathCost == self.visited_nodes[i].pathCost)):
                # print("________visited already")
                return True
            else:
                # print("+++++++++++not visited")
                return False



