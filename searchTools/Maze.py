import random
import turtle

from Objects import Cell
from searchTools import Location


class Maze():
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cells = [[Cell.Cell() for _ in range(height + 2)] for _ in range(width + 2)]
        self.visited = [[False for _ in range(height + 2)] for _ in range(width + 2)]
        self.pokes_locations = []
        self.define_initial_state()
        self.startLocation = self.gen_random_location()
        self.endLocation = self.gen_random_location()
        self.gen_maze()

    def define_initial_state(self):

        for x in range(0, self.width + 2):
            self.visited[x][0] = True
            self.visited[x][self.height + 1] = True

        for y in range(0, self.height + 2):
            self.visited[0][y] = True
            self.visited[self.width + 1][y] = True

    def generate_maze(self, startX, startY):
        self.visited[startX][startY] = True
        while (not self.visited[startX][startY + 1]) or (not self.visited[startX + 1][startY]) or (
                not self.visited[startX][startY - 1]) or (not self.visited[startX - 1][startY]):
            while (True):
                # Choose a direction to move to 1 = North, 2 = East , 3 = South , 4 = West
                chosen_direction = random.randint(1, 4)
                if chosen_direction == 1 and not self.visited[startX][startY + 1]:
                    self.cells[startX][startY].north = False
                    self.cells[startX][startY + 1].south = False
                    self.generate_maze(startX, startY + 1)
                    break
                if chosen_direction == 2 and not self.visited[startX + 1][startY]:
                    self.cells[startX][startY].east = False
                    self.cells[startX + 1][startY].west = False
                    self.generate_maze(startX + 1, startY)
                    break
                if chosen_direction == 3 and not self.visited[startX][startY - 1]:
                    self.cells[startX][startY].south = False
                    self.cells[startX][startY - 1].north = False
                    self.generate_maze(startX, startY - 1)
                    break
                if chosen_direction == 4 and not self.visited[startX - 1][startY]:
                    self.cells[startX][startY].west = False
                    self.cells[startX - 1][startY].east = False
                    self.generate_maze(startX - 1, startY)
                    break

    def gen_maze(self):
        if (self.startLocation.x == self.endLocation.x and self.startLocation.y == self.endLocation.y):
            self.endLocation = self.gen_random_location()
        self.generate_maze(self.startLocation.x, self.startLocation.y)
        self.gen_pokes(random.randint(1, self.width/2))
        self.draw_maze()

    def gen_random_location(self):
        loc = Location.Location(random.randint(1, self.width), random.randint(1, self.height))
        return loc

    def gen_pokes(self, number_of_pokes):
        print(number_of_pokes)
        for i in range(0, number_of_pokes):
            loc = self.gen_random_location()
            self.cells[loc.x][loc.y].hasPokemon = True
            self.pokes_locations.append(loc)


    def draw_maze(self):
        # Initialise Window with its attributes
        turtle.title("Pokemon Maze")
        window = turtle.Screen()
        turtle.setworldcoordinates(0, 0, self.width + 0.5, self.height + 0.5)
        window.bgcolor("white")

        # Initialise my drawing Turtle
        drawingTurtle = turtle.Turtle()
        drawingTurtle.speed(0)
        for x in range(1, self.width + 1):
            for y in range(1, self.height + 1):
                drawingTurtle.penup()
                drawingTurtle.setpos(x - 1, y - 1)
                cell = self.cells[x][y]
                if cell.south:
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor() + 1, drawingTurtle.ycor())
                if cell.east:
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor(), drawingTurtle.ycor() + 1)
                if cell.north:
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor() - 1, drawingTurtle.ycor())
                if cell.west:
                    drawingTurtle.pendown()
                else:
                    drawingTurtle.penup()
                drawingTurtle.setpos(drawingTurtle.xcor(), drawingTurtle.ycor() - 1)
        window.exitonclick()
