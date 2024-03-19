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


def decode_maze(maze_str):
    lines = maze_str.strip().split('\n')

    decoded_maze = []

    for line in lines:
        row = []
        for i in range(len(line)):
            if line[i] == '#':
                row.append(1)
            elif line[i] == ' ' and i % 2 == 0:
                row.append(0)

        decoded_maze.append(row)

    return decoded_maze


# Example usage:
maze = decode_maze(given_maze)