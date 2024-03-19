from collections import deque
from algo.solve import Solve


class BFS(Solve):
    def __init__(
        self,
        maze: list[list[int]],
        sy: int,
        sx: int,
        ey: int,
        ex: int
    ):
        super().__init__(maze, sy, sx, ey, ex)

    def algo(self) -> int | bool:
        queue = deque([(self.sy, self.sx)])
        visited = [[0] * len(self.maze) for _ in range(len(self.maze[0]))]
        moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            row, col = queue.popleft()
            visited[row][col] = 1
            if row == self.ey and col == self.ex:
                return visited

            for move in moves:
                new_row = row + move[0]
                new_col = col + move[1]
                if self.valid_move(new_row, new_col) and visited[new_row][new_col] == 0:
                    queue.append((new_row, new_col))

        return False
