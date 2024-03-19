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


def print_maze():
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                print("#", end=" ")
            else:
                try:
                    print(".", end=" ") if visited[row][col] else print(
                        " ", end=" ")
                except:
                    print(" ", end=" ")
        print()


def print_step(algo: str, step: int):
    print(f'Step needed for {algo} is {step}')
    print_maze()
    print()

# ---------------------------------------------------------------


""" visited = [[0] * width for _ in range(height)]
dijkstra = Dijkstra(maze, visited, sy, sx, ey, ex, 1, [
    (1, 0), (-1, 0), (0, -1), (0, 1)])
dijkstra_steps = dijkstra.algo()
print_step("dijkstra", dijkstra_steps)


visited = [[0] * width for _ in range(height)]
dfs = DFS(maze, visited, sy, sx, ey, ex, 1, [
    (1, 0), (-1, 0), (0, -1), (0, 1)])
dfs_steps = dfs.algo()
print_step("dfs", dfs_steps)


visited = [[0] * width for _ in range(height)]
bfs = BFS(maze, visited, sy, sx, ey, ex, 1, [
    (1, 0), (-1, 0), (0, -1), (0, 1)])
bfs_steps = bfs.algo()
print_step("bfs", bfs_steps) """


visited = [[0] * width for _ in range(height)]
hand_ons = HandOns(maze, visited, sy, sx, ey, ex, 1, [
    (1, 0), (-1, 0), (0, -1), (0, 1)])
hand_ons_step = hand_ons.algo()
print_step("hand on wall", hand_ons_step)

# ---------------------------------------------------------------
