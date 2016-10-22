from objects import Maze
from objects.Enums import Search
from searchTools.CatchemProblem import CatchEmProblem
from searchTools.GeneralSearch import GeneralSearch




maze = Maze.Maze(7,7)
problem = CatchEmProblem(maze)
search = GeneralSearch(problem, Search.AS, 3)
node = search.search()
# print (str(node))
print("Search is successfully over!")

