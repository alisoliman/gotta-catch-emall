# import stddraw

class Maze():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.north = [[x for x in range(width)] for y in range(height)]
        self.south = [[x for x in range(width)] for y in range(height)]
        self.east = [[x for x in range(width)] for y in range(height)]
        self.west = [[x for x in range(width)] for y in range(height)]
        self.visited = [[False]*(width+2)]*(height+2)
        # stddraw.setXscale(0,width+2)
        # stddraw.setYscale(0,height+2)



    # def genMaze(self):
    #     for


