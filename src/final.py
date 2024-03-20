from algo.dfs import DFS
from algo.bfs import BFS
from algo.dijkstra import Dijkstra
from algo.handons import HandOns
given_maze = """
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     #               #                                   #
# #   #   # # # # #   # # # # # # #   #   #   # # # # # # #
#         #       #               #   #   #   #           #
#   # # # #   #   # # # # #   #   # # #   #   #   # # #   #
#     #       #   #       #   #   #       #   #       #   #
# #   #   # # #   #   #   #   #   #   # # #   # # #   #   #
      #       #       #                   #       #   #   #
# # # # # #   # # # # # # # # # # # # # # #   #   # # #   #
#         #           #           #       #   #   #       #
# # #   # # # #   #   #   # # #   #   #   #   #   #   # # #
#             #   #   #       #       #   #   #   #       #
#   # # # #   #   #   # # #   # # # # #   #   #   # # #   #
#       #     #   #       #           #       #       #   #
# # #   #   # # # # # #   # # # # #   # # # # # # #   #   #
#       #                 #       #   #       #       #   #
#   #   # # # # # # # # # #   #   #   #   # # #   # # #   #
#   #       #                 #       #           #       #
# # # # #   # # # # # #   # # # # # # #   # # # # #   # # #
#       #       #     #   #       #   #           #       #
#   #   # # #   #   # #   # # #   #   #   # # #   # # #   #
#   # # #       #     #           #       #   #       #   #
#   #       # # # #   # # # # #   # # # # #   # # #   #   #
#   #   #   #         #           #       #       #       #
#   #   #   # #   # # #   #   # # # # #   #   #   # # # # #
#   #   #         #       #           #       #   #       #
#   #   # # # #   #   # # # # #   #   # # # # #   #   #   #
#   #   #     #   #       #   #   #           #       #    
#   #   #     # # # # #   #   #   # # # # #   # # #   #   #
#       #                 #       #                   #   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""


def decode_maze(maze_str) -> list:
    lines = maze_str.strip().split('\n')

    decoded_maze = []

    for line in lines:
        row = []
        for i in range(0, len(line), 2):
            if line[i] == '#':
                row.append(1)
            elif line[i] == ' ':
                row.append(0)

        decoded_maze.append(row)

    return decoded_maze


maze = decode_maze(given_maze)
for i in maze:
    print(i)

""" for i in range(len(maze)):
    if maze[i][len(maze[0]) - 1] == 0:
        print(i)
        break """

sy, sx = 7, 0
ey, ex = 27, len(maze[0]) - 1


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

print("Dijkstra")
dijkstra = Dijkstra(maze, sy, sx, ey, ex)
dijkstra_visited = dijkstra.algo()
dijkstra_step = print_maze(dijkstra_visited)
print(dijkstra_step)

print("Wall Following")
hand_ons = HandOns(maze, sy, sx, ey, ex)
hand_ons_visited = hand_ons.algo()
hand_ons_step = print_maze(hand_ons_visited)
print(hand_ons_step)
