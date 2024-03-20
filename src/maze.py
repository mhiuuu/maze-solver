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


# ---------------------------------------------------------------


print("Dijkstra")
dijkstra = Dijkstra(maze, sy, sx, ey, ex)
dijkstra_visited = dijkstra.algo()
dijkstra_step = print_maze(dijkstra_visited)
print(dijkstra_step)

print("DFS")
dfs = DFS(maze, sy, sx, ey, ex)
dfs_visited = dfs.algo()
dfs_step = print_maze(dfs_visited)
print(dfs_step)

print("BFS")
bfs = BFS(maze, sy, sx, ey, ex)
bfs_visited = bfs.algo()
bfs_step = print_maze(bfs_visited)
print(bfs_step)

print("Wall Following")
hand_ons = HandOns(maze, sy, sx, ey, ex)
hand_ons_visited = hand_ons.algo()
hand_ons_step = print_maze(hand_ons_visited)
print(hand_ons_step)

# ---------------------------------------------------------------
""" dfs_stats, bfs_stats, dijkstra_stats, wallfollowing_stats = [], [], [], []


def get_step(visited: list) -> int:
    step = 0
    for i in visited:
        for j in i:
            if j == 1:
                step += 1
    return step


for i in range(10, 100):
    width = i
    height = i
    generator = MazeGenerator(width, height)
    generator.create_maze(1, 1)
    maze = generator.get_maze()
    # -------------------------------------------------------------------------------
    ey, ex = random.randint(1, height - 2), width - 1 + (width % 2 == 0)
    while maze[ey][ex-1] == 1:
        ey = random.randint(1, height - 2)
    maze[ey][ex] = 0
    sy, sx = random.randint(1, height - 2), 0
    while maze[sy][sx+1] == 1:
        sy = random.randint(1, height - 2)
    maze[sy][sx] = 0
    # -------------------------------------------------------------------------------
    dijkstra = Dijkstra(maze, sy, sx, ey, ex)
    dijkstra_visited = dijkstra.algo()
    dijkstra_stats.append(get_step(dijkstra_visited))

    dfs = DFS(maze, sy, sx, ey, ex)
    dfs_visited = dfs.algo()
    dfs_stats.append(get_step(dfs_visited))

    bfs = BFS(maze, sy, sx, ey, ex)
    bfs_visited = bfs.algo()
    bfs_stats.append(get_step(bfs_visited))

    hand_ons = HandOns(maze, sy, sx, ey, ex)
    hand_ons_visited = hand_ons.algo()
    wallfollowing_stats.append(get_step(hand_ons_visited))
 """
