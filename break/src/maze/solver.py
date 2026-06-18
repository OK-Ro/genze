from src.maze.cell import Cell


class MazeSolver:
    def __init__(self, grid: list[list[Cell]], entry: tuple[int, int], exit: tuple[int, int]):
        self.grid = grid
        self.entry = entry
        self.exit = exit
        self.height = len(grid)
        self.width = len(grid[0])

        self.path: list[tuple[int, int]] = []
        self.visited: set[tuple[int, int]] = set()

    def solve(self) -> list[tuple[int, int]]:
        start_x, start_y = self.entry

        if self._dfs(start_x, start_y):
            return self.path

        return []

    def _dfs(self, x: int, y: int) -> bool:
        # goal reached
        if (x, y) == self.exit:
            self.path.append((x, y))
            return True

        # mark visited
        self.visited.add((x, y))
        self.path.append((x, y))

        cell = self.grid[y][x]

        # directions: (dx, dy, wall, opposite wall not needed here)
        moves = [
            (0, -1, "N"),
            (1, 0, "E"),
            (0, 1, "S"),
            (-1, 0, "W"),
        ]

        for dx, dy, wall in moves:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < self.width and 0 <= ny < self.height):
                continue

            if (nx, ny) in self.visited:
                continue

            # IMPORTANT: can only move if NO wall
            if cell.has_wall(wall):
                continue

            if self._dfs(nx, ny):
                return True

        # backtrack
        self.path.pop()
        return False