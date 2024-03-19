import heapq
from algo.solve import Solve


class Dijkstra(Solve):
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
        distances = [[float('inf')] * len(self.maze[0])
                     for _ in range(len(self.maze))]
        visited = [[0] * len(self.maze) for _ in range(len(self.maze[0]))]
        moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        distances[self.sy][self.sx] = 0

        priority_queue = [(0, (self.sy, self.sx))]

        while priority_queue:
            distance, (row, col) = heapq.heappop(priority_queue)

            if (row, col) == (self.ey, self.ex):
                return visited

            if distance > distances[row][col]:
                continue

            for move in moves:
                new_row = row + move[0]
                new_col = col + move[1]

                if self.valid_move(new_row, new_col):
                    new_distance = distance + 1

                    if new_distance < distances[new_row][new_col]:
                        distances[new_row][new_col] = new_distance
                        heapq.heappush(
                            priority_queue,
                            (new_distance, (new_row, new_col))
                        )
                        visited[new_row][new_col] = 1

        return False
