import random
from generator import MazeGenerator
from algo.dfs import DFS
from algo.bfs import BFS
from algo.dijkstra import Dijkstra
from algo.handons import HandOns
from algo.astar import AStar
# ---------------------------------------------------------------

width, height = 15, 15
generator = MazeGenerator(width, height)
generator.create_maze(1, 1)
maze = generator.get_maze()

# ---------------------------------------------------------------

sy, sx = random.randint(1, height - 2), 0
while maze[sy][sx+1] == 1:
    sy = random.randint(1, height - 2)
maze[sy][sx] = 0

ey, ex = random.randint(1, height - 2), width - 1 + (width % 2 == 0)
while maze[ey][ex-1] == 1:
    ey = random.randint(1, height - 2)
maze[ey][ex] = 0

# ---------------------------------------------------------------


def print_maze(visited: list[list[int]] = []) -> int:
    step = 0
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                print("#", end=" ")
            else:
                try:
                    if visited[row][col]:
                        print(".", end=" ")
                        step += 1
                    else:
                        print(" ", end=" ")
                except:
                    print(" ", end=" ")
        print()
    return step


def print_step(algo: str, step: int):
    print(f'Step needed for {algo} is {step}')
    print_maze()
    print()

# ---------------------------------------------------------------


dijkstra = Dijkstra(maze, sy, sx, ey, ex)
dijkstra_visited = dijkstra.algo()
dijkstra_step = print_maze(dijkstra_visited)
print(dijkstra_step)

dfs = DFS(maze, sy, sx, ey, ex)
dfs_visited = dfs.algo()
dfs_step = print_maze(dfs_visited)
print(dfs_step)


bfs = BFS(maze, sy, sx, ey, ex)
bfs_visited = bfs.algo()
bfs_step = print_maze(bfs_visited)
print(bfs_step)


hand_ons = HandOns(maze, sy, sx, ey, ex)
hand_ons_visited = hand_ons.algo()
hand_ons_step = print_maze(hand_ons_visited)
print(hand_ons_step)

astar = AStar(maze, sy, sx, ey, ex)
astar_visited = astar.algo()
astar_step = print_maze(astar_visited)
print(astar_step)
# ---------------------------------------------------------------
