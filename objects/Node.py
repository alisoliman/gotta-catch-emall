class Node():
    def __init__(self, state, parent=None, op=None, depth = 0, pathCost=0):
        self.state = state
        self.parent = parent
        self.operation = op
        self.depth = depth
        if parent:
            self.depth = parent.depth + 1
        self.pathCost = pathCost