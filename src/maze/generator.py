from typing import Any
import random

from src.maze.cell import Cell, N, E, S, W


# Opposite directions (important for wall consistency)
OPPOSITE = {
    N: S,
    S: N,
    E: W,
    W: E,
}

# (direction, dx, dy)
DIRECTIONS = [
    (N, 0, -1),
    (E, 1, 0),
    (S, 0, 1),
    (W, -1, 0),
]


class MazeGenerator:
    def __init__(self, config: dict[str, Any]) -> None:
        # ---- CONFIG VALUES ----
        self.width: int = config["WIDTH"]
        self.height: int = config["HEIGHT"]
        self.entry: tuple[int, int] = config["ENTRY"]
        self.exit: tuple[int, int] = config["EXIT"]
        self.perfect: bool = config["PERFECT"]
        self.seed = config.get("SEED")

        # maze grid
        self.grid: list[list[Cell]] = []

    # --------------------------
    # CREATE INITIAL GRID
    # --------------------------
    def _create_grid(self) -> list[list[Cell]]:
        """
        Create a fully closed grid:
        every cell starts with 4 walls (1111)
        """
        return [
            [Cell() for _ in range(self.width)]
            for _ in range(self.height)
        ]

    # --------------------------
    # DFS CARVING (CORE MAZE)
    # --------------------------
    def _carve(self, x: int, y: int, visited: set) -> None:
        """
        Depth-first search maze generation.
        Removes walls between cells.
        """
        visited.add((x, y))

        # randomize directions for randomness
        directions = DIRECTIONS[:]
        random.shuffle(directions)

        for direction, dx, dy in directions:
            nx, ny = x + dx, y + dy

            # check bounds
            if 0 <= nx < self.width and 0 <= ny < self.height:

                # if not visited, carve path
                if (nx, ny) not in visited:

                    # remove wall between current cell and next cell
                    self.grid[y][x].remove_wall(direction)
                    self.grid[ny][nx].remove_wall(OPPOSITE[direction])

                    # continue recursion
                    self._carve(nx, ny, visited)

    # --------------------------
    # OPEN ENTRY & EXIT
    # --------------------------
    def _open_entry_exit(self) -> None:
        """
        Ensure ENTRY and EXIT are open to outside.
        This is REQUIRED after generation.
        """

        ex, ey = self.entry
        self.grid[ey][ex].remove_wall(N)  # open entry

        ex, ey = self.exit
        self.grid[ey][ex].remove_wall(S)  # open exit

    # --------------------------
    # GENERATE MAZE
    # --------------------------
    def generate(self) -> list[list[Cell]]:
        """
        Main function:
        1. initialize grid
        2. set seed (if any)
        3. carve maze
        4. open entry/exit
        5. return result
        """

        # seed for reproducibility
        if self.seed is not None:
            random.seed(self.seed)

        # step 1: create grid
        self.grid = self._create_grid()

        # step 2: carve maze starting from ENTRY
        visited = set()
        self._carve(self.entry[0], self.entry[1], visited)

        # step 3: open entry & exit
        self._open_entry_exit()

        return self.grid

def generate_maze(config: dict[str, Any]) -> list[list[int]]:
    return MazeGenerator(config).generate()
