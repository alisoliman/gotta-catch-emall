import Maze
from objects.Enums import Search
from searchTools.CatchemProblem import CatchEmProblem
from searchTools.GeneralSearch import GeneralSearch




maze = Maze.Maze(2, 2)
problem = CatchEmProblem(maze)
search = GeneralSearch(problem, Search.BF, 3)
node = search.search()
# print (str(node))
print("Search is successfully over!")

