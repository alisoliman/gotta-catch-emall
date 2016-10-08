# import stddraw
import random

import numpy
import turtle

import Cell

class Maze():
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cells = [[Cell.Cell() for x in range(height + 2)] for y in range(width + 2)]
        self.visited = [[False for x in range(height+2)] for y in range(width+2)]
        self.defineInitialState()
        # stddraw.setXscale(0,width+2)
        # stddraw.setYscale(0,height+2)


    def defineInitialState(self):

        for x in range(0,self.width+2):
            self.visited[x][0] = True
            self.visited[x][self.height+1] = True



        for y in range(0,self.height+2):
            self.visited[0][y] = True
            self.visited[self.width+1][y] = True



    def genMaze(self):
        startX = random.randint(1, self.width)
        startY = random.randint(1, self.height)
        self.genMaze(startX,startY)



    def genMaze(self,startX,startY):
        self.visited[startX][startY] = True
        while (not self.visited[startX][startY+1] or (not self.visited[startX+1][startY]) ):