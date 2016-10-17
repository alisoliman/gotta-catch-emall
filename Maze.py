from stddraw import color
import random
import Cell
import turtle


class Maze():
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cells = [[Cell.Cell() for x in range(height + 2)] for y in range(width + 2)]
        self.visited = [[False for x in range(height + 2)] for y in range(width + 2)]
        self.defineInitialState()
        startX = random.randint(1, self.width)
        startY = random.randint(1, self.height)
        self.genMaze(startX, startY)
        self.drawMaze()

        # stddraw.setXscale(0,width+2)
        # stddraw.setYscale(0,height+2)
        # stddraw._showAndWaitForever()

    def defineInitialState(self):

        for x in range(0, self.width + 2):
            self.visited[x][0] = True
            self.visited[x][self.height + 1] = True

        for y in range(0, self.height + 2):
            self.visited[0][y] = True
            self.visited[self.width + 1][y] = True

    def genMaze(self, startX, startY):
        self.visited[startX][startY] = True
        while (not self.visited[startX][startY + 1]) or (not self.visited[startX + 1][startY]) or (
        not self.visited[startX][startY - 1]) or (not self.visited[startX - 1][startY]):
            while (True):
                chosen_direction = random.randint(1,4)  # Choose a direction to move to 1 = North, 2 = East , 3 = South , 4 = West
                if chosen_direction == 1 and not self.visited[startX][startY + 1]:
                    self.cells[startX][startY].north = False
                    self.cells[startX][startY + 1].south = False
                    self.genMaze(startX, startY + 1)
                    break
                if chosen_direction == 2 and not self.visited[startX + 1][startY]:
                    self.cells[startX][startY].east = False
                    self.cells[startX + 1][startY].west = False
                    self.genMaze(startX + 1, startY)
                    break
                if chosen_direction == 3 and not self.visited[startX][startY - 1]:
                    self.cells[startX][startY].south = False
                    self.cells[startX][startY - 1].north = False
                    self.genMaze(startX, startY - 1)
                    break
                if chosen_direction == 4 and not self.visited[startX - 1][startY]:
                    self.cells[startX][startY].west = False
                    self.cells[startX - 1][startY].east = False
                    self.genMaze(startX - 1, startY)
                    break

    def drawMaze(self):
        # Initialise Window with its attributes
        turtle.title("Pokemon Maze")
        window = turtle.Screen()
        turtle.setworldcoordinates(0, 0, self.width+0.5, self.height+0.5)
        window.bgcolor("white")
        print(window.screensize())

        # Initialise my drawing Turtle
        drawingTurtle = turtle.Turtle()
        drawingTurtle.speed(0)
        # cell = self.cells[1][1]
        # x = 1
        # y = 1
        # print(cell.south)
        # print(cell.north)
        # print(cell.east)
        # print(cell.west)
        for x in range(1,self.width+1):
            for y in range(1,self.height+1):
                drawingTurtle.penup()
                drawingTurtle.setpos(x-1, y-1)
                cell = self.cells[x][y]
                if (x == 1):
                    print(cell.east)
                if cell.south :
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor() + 1, drawingTurtle.ycor())
                if cell.east:
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor(), drawingTurtle.ycor()+1)
                if cell.north:
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor() - 1, drawingTurtle.ycor())
                if cell.west:
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor(), drawingTurtle.ycor()-1)






        # for x in range(1,self.width):
        #     for y in range(1,self.height):
        #         if self.cells[x][y].south: drawingTurtle.setx(drawingTurtle.xcor()+1)
        window.exitonclick()

    def drawCell(self, cell):
        if cell.north == False:
            return
