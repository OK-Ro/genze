from genze.break.src.maze.cell import Cell


class Pattern42:
    def apply(self, grid: list[list[Cell]]) -> None:
        height = len(grid)
        width = len(grid[0])

        if width < 12 or height < 7:
            print("⚠ Pattern 42 skipped: maze too small")
            return

        start_x = width // 2 - 5
        start_y = height // 2 - 2

        # shape of 4
        four = [
            (0, 0),
            (0, 1),
            (0, 1),
            (0, 2),
            (1, 2),
            (2, 2),
            (3, 0),
            (3, 1),
            (3, 2),
            (3, 3),
            (3, 4),
        ]

        # shape of 2 (UPDATED: added missing top bar)
        two = [
            (6, 0),
            (6, 2),
            (6, 3),
            (6, 4),
            (7, 0),
            (7, 2),
            (7, 4),
            (8, 0),
            (8, 1),
            (8, 2),
            (8, 4),
        ]

        for dx, dy in four + two:
            x = start_x + dx
            y = start_y + dy

            if 0 <= x < width and 0 <= y < height:
                grid[y][x].pattern_42 = True
