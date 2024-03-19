from collections import deque
from algo.solve import Solve


class BFS(Solve):
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
        queue = deque([(self.sy, self.sx)])

        while queue:
            row, col = queue.popleft()
            self.visited[row][col] = self.step
            if row == self.ey and col == self.ex:
                return self.step

            for move in self.moves:
                new_row = row + move[0]
                new_col = col + move[1]
                if self.valid_move(new_row, new_col) and self.visited[new_row][new_col] == 0:
                    queue.append((new_row, new_col))
                    self.step += 1

        return False
