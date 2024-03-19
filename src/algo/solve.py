class Solve:
    def __init__(
        self,
        maze: list[list[int]],
        sy: int,
        sx: int,
        ey: int,
        ex: int,
    ):
        self.maze = maze
        self.sy = sy
        self.sx = sx
        self.ey = ey
        self.ex = ex

    def valid_move(self, row: int, col: int) -> bool:
        return 0 <= row < len(self.maze) and 0 <= col < len(self.maze[0]) and self.maze[row][col] == 0
