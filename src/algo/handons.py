from algo.solve import Solve


class HandOns(Solve):
    def __init__(
        self,
        maze: list[list[int]],
        visited: list[list[int]],
        sy: int,
        sx: int,
        ey: int,
        ex: int,
        step: int,
        moves: list[tuple]
    ):
        super().__init__(maze, visited, sy, sx, ey, ex, step, moves)

    def algo(self) -> int | bool:
        left_directions = {
            (0, 1): (-1, 0),
            (1, 0): (0, 1),
            (0, -1): (1, 0),
            (-1, 0): (0, -1)
        }
        direction = (0, 1)
        row, col = self.sy, self.sx
        while True:
            if not self.visited[row][col]:
                self.step += 1
            self.visited[row][col] = self.step
            if row == self.ey and col == self.ex:
                return self.step

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
