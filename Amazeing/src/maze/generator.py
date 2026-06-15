"""Module handling procedural maze layout generation routines via DFS."""

import random
from typing import Any
from src.maze.cell import Cell
from src.algorithms.dfs import DFSAlgorithm


class MazeGenerator:
    """Handles core procedural layout carving routines across a grid of cells."""

    def __init__(self, config: dict[str, Any]) -> None:
        """Initialize parameters, parse bounds, and set up random seeds."""
        self.width: int = config["WIDTH"]
        self.height: int = config["HEIGHT"]
        self.entry: tuple[int, int] = config["ENTRY"]
        self.exit: tuple[int, int] = config["EXIT"]
        self.perfect: bool = config["PERFECT"]

        self.seed: int = config.get("SEED", 42)
        random.seed(self.seed)

        self.grid: list[list[Cell]] = []

    def _create_grid(self) -> list[list[Cell]]:
        return [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]

    def _get_unvisited_neighbors(self, cell: Cell) -> list[tuple[Cell, str, str]]:
        """Find adjacent cells that have not been visited yet.

        Returns:
            A list of tuples matching: (Neighbor Cell, Direct Wall, Opposite Wall)
        """
        neighbors = []

        directions = [
            (0, -1, "N", "S"),  # North neighbor
            (1, 0, "E", "W"),  # East neighbor
            (0, 1, "S", "N"),  # South neighbor
            (-1, 0, "W", "E"),  # West neighbor
        ]

        for dx, dy, current_wall, neighbor_wall in directions:
            nx, ny = cell.x + dx, cell.y + dy

            # Ensure boundary safety checks pass
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbor_cell = self.grid[ny][nx]
                if not neighbor_cell.visited:
                    neighbors.append((neighbor_cell, current_wall, neighbor_wall))

        return neighbors

    def generate(self) -> list[list[str]]:
        self.grid = self._create_grid()

        # algo = DFSAlgorithm()
        # algo.carve(self.grid, self.entry)

        en_x, en_y = self.entry
        ex_x, ex_y = self.exit

        if en_y == 0:
            self.grid[en_y][en_x].remove_wall("N")
        elif en_x == 0:
            self.grid[en_y][en_x].remove_wall("W")

        if ex_y == self.height - 1:
            self.grid[ex_y][ex_x].remove_wall("S")
        elif ex_x == self.width - 1:
            self.grid[ex_y][ex_x].remove_wall("E")

        hex_string_grid: list[list[str]] = []
        for row in self.grid:
            hex_row = [cell.to_hex() for cell in row]
            hex_string_grid.append(hex_row)

        return hex_string_grid


def generate_maze(config: dict[str, Any]) -> list[list[str]]:
    """Helper functional hook for global imports."""
    return MazeGenerator(config).generate()
