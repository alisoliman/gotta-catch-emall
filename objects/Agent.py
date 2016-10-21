from objects import Maze
from searchTools.CatchemProblem import CatchEmProblem
from searchTools.GeneralSearch import GeneralSearch




maze = Maze.Maze(4,4)
problem = CatchEmProblem(maze)
search = GeneralSearch(problem)
print (search)

