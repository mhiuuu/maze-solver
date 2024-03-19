import heapq
from algo.solve import Solve


class Dijkstra(Solve):
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
        distances = [[float('inf')] * len(self.maze[0])
                     for _ in range(len(self.maze))]
        distances[self.sy][self.sx] = 0

        priority_queue = [(0, (self.sy, self.sx))]

        while priority_queue:
            distance, (row, col) = heapq.heappop(priority_queue)

            if (row, col) == (self.ey, self.ex):
                return distance

            if distance > distances[row][col]:
                continue

            for move in self.moves:
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
                        self.visited[new_row][new_col] = distance

        return False
