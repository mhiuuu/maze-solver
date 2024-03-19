from algo.solve import Solve
import heapq


class AStar(Solve):
    def __init__(
        self,
        maze: list[list[int]],
        sy: int,
        sx: int,
        ey: int,
        ex: int,
    ):
        super().__init__(maze, sy, sx, ey, ex)
        self.visited = [[False for _ in range(
            len(maze[0]))] for _ in range(len(maze))]

    def algo(self) -> int | bool:
        rows, cols = len(self.maze), len(self.maze[0])
        start = (self.sy, self.sx)
        goal = (self.ey, self.ex)
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            current = heapq.heappop(open_set)[1]
            # Mark the current cell as visited
            self.visited[current[0]][current[1]] = True
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (current[0] + dr, current[1] + dc)
                if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and self.maze[neighbor[0]][neighbor[1]] == 0:
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + \
                            self.heuristic(neighbor, goal)
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return None

    def heuristic(self, start, goal):
        # Manhattan distance heuristic
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])
