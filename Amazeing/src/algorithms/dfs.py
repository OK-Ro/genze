"""Module implementing the Randomized Depth-First Search maze carving algorithm."""

import random
from src.maze.cell import Cell
from src.algorithms.base import BaseAlgorithm


class DFSAlgorithm(BaseAlgorithm):
    """Carves mazes using a randomized backtracking stack (Depth-First Search)."""

    def _get_unvisited_neighbors(
        self, cell: Cell, grid: list[list[Cell]], width: int, height: int
    ) -> list[tuple[Cell, str, str]]:

        neighbors = []
        directions = [
            (0, -1, "N", "S"),  # North
            (1, 0, "E", "W"),  # East
            (0, 1, "S", "N"),  # South
            (-1, 0, "W", "E"),  # West
        ]

        for dx, dy, cur_wall, opp_wall in directions:
            nx, ny = cell.x + dx, cell.y + dy
            if 0 <= nx < width and 0 <= ny < height:
                neighbor_cell = grid[ny][nx]
                if not neighbor_cell.visited:
                    neighbors.append((neighbor_cell, cur_wall, opp_wall))
        return neighbors

    def carve(self, grid: list[list[Cell]], start_at: tuple[int, int]) -> None:
        height = len(grid)
        width = len(grid[0]) if height > 0 else 0

        start_x, start_y = start_at
        current_cell = grid[start_y][start_x]
        current_cell.visited = True

        stack: list[Cell] = [current_cell]

        while stack:
            current_cell = stack[-1]
            unvisited = self._get_unvisited_neighbors(current_cell, grid, width, height)

            if unvisited:
                next_cell, cur_wall, opp_wall = random.choice(unvisited)
                current_cell.remove_wall(cur_wall)
                next_cell.remove_wall(opp_wall)
                next_cell.visited = True
                stack.append(next_cell)
            else:
                stack.pop()
