from objects import Maze
from objects.Enums import Search
from searchTools.CatchemProblem import CatchEmProblem
from searchTools.GeneralSearch import GeneralSearch




maze = Maze.Maze(4,4)
problem = CatchEmProblem(maze)
search = GeneralSearch(problem, Search.BF)
node = search.search()
print (node)

