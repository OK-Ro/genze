from typing import Any
from src.maze.cell import Cell
from src.algorithms.dfs import DFS_Algorithm
import random

class MazeGenerator:
    def __init__(self, config: dict[str, Any]) -> None:
        self.width: int = config["WIDTH"]
        self.height: int = config["HEIGHT"]
        self.entry: tuple[int, int] = config["ENTRY"]
        self.exit: tuple[int, int] = config["EXIT"]
        self.output_file: str = config["OUTPUT_FILE"]
        self.perfect: bool = config["PERFECT"]
        self.seed: int = config.get("SEED", 42)
        self.pattern: int = config.get("PATTERN_42", 42)
        random.seed(None)
        self.grid: list[list[Cell]] = []

    def _create_grid(self) -> list[list[Cell]]:
        self.grid = [
            [Cell(x, y) for x in range(self.width)] for y in range(self.height)
        ]

        return self.grid

    def generate(self) -> list[list[str]]:
        self.grid = self._create_grid()

        algo = DFS_Algorithm()
        algo.carve(self.grid, self.entry, self.width, self.height)

        entry_x, entry_y = self.entry
        entry_cell = self.grid[entry_y][entry_x]

        entry_cell.remove_wall("W")

        exit_x, exit_y = self.exit
        exit_cell = self.grid[exit_y][exit_x]

        exit_cell.remove_wall("E")

        hex_grid_string: list[list[str]] = []
        for row in self.grid:
            hex_grid = [cell._convert_to_hex() for cell in row]
            hex_grid_string.append(hex_grid)
        return hex_grid_string


def generate_maze(config: dict[str, Any]) -> list[list[str]]:
    return MazeGenerator(config).generate()
