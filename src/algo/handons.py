from algo.solve import Solve


class HandOns(Solve):
    def __init__(
        self,
        maze: list[list[int]],
        sy: int,
        sx: int,
        ey: int,
        ex: int,
    ):
        super().__init__(maze, sy, sx, ey, ex)

    def algo(self) -> int | bool:
        left_directions = {
            (0, 1): (-1, 0),
            (1, 0): (0, 1),
            (0, -1): (1, 0),
            (-1, 0): (0, -1)
        }
        direction = (0, 1)
        row, col = self.sy, self.sx
        visited = [[0] * len(self.maze) for _ in range(len(self.maze[0]))]

        while True:
            visited[row][col] = 1
            if row == self.ey and col == self.ex:
                return visited

            if not self.valid_move(row + left_directions[direction][0], col + left_directions[direction][1]):
                if not self.valid_move(row + direction[0], col + direction[1]):
                    direction = (direction[0] * -1, direction[1] * -1)
                    direction = left_directions[direction]
                else:
                    row += direction[0]
                    col += direction[1]
            else:
                direction = left_directions[direction]
                row += direction[0]
                col += direction[1]
