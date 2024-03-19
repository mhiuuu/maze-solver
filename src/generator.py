import random


class MazeGenerator:
    def __init__(self, width: int, height: int):
        self.width = width // 2 * 2 + 1
        self.height = height // 2 * 2 + 1
        self.cells = [
            [1] * self.width for _ in range(self.height)
        ]

    def set_path(self, x: int, y: int):
        self.cells[y][x] = 0

    def set_wall(self, x: int, y: int):
        self.cells[y][x] = 1

    def is_wall(self, x: int, y: int) -> int | bool:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        return False

    def create_maze(self, start_x: int, start_y: int):
        stack = [(start_x, start_y)]

        while stack:
            x, y = stack[-1]
            self.set_path(x, y)

            all_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            random.shuffle(all_directions)

            found = False
            for direction_to_try in all_directions:
                node_x = x + (direction_to_try[0] * 2)
                node_y = y + (direction_to_try[1] * 2)

                if 0 <= node_x < self.width and 0 <= node_y < self.height and self.is_wall(node_x, node_y):
                    link_cell_x = x + direction_to_try[0]
                    link_cell_y = y + direction_to_try[1]
                    self.set_path(link_cell_x, link_cell_y)
                    stack.append((node_x, node_y))
                    found = True
                    break

            if not found:
                stack.pop()

    def get_maze(self) -> list[list[int]]:
        return self.cells
