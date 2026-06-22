from genze.break.src.algorithms.path import MazeAlgorithms
from src.maze.cell import Cell
import random


class DFS_Algorithm(MazeAlgorithms):

    def _get_unvisited_neighbors(
        self, cell: Cell, grid: list[list[Cell]], width: int, height: int
    ) -> list[tuple[Cell, str, str]]:

        possible_moves: list[tuple[Cell, str, str]] = []

        directions = [
            (0, -1, "N", "S"),  # move up
            (1, 0, "E", "W"),  # move right
            (0, 1, "S", "N"),  # move down
            (-1, 0, "W", "E"),  # move left
        ]

        for dx, dy, direction, opposite_direction in directions:

            next_x = cell.x + dx
            next_y = cell.y + dy

            # check bounds
            if 0 <= next_x < width and 0 <= next_y < height:

                next_cell = grid[next_y][next_x]

                if not next_cell.visited:
                    possible_moves.append((next_cell, direction, opposite_direction))

        return possible_moves

    def carve(
        self, grid: list[list[Cell]], start_at: tuple[int, int], width: int, height: int
    ) -> None:

        start_x, start_y = start_at

        active_cell = grid[start_y][start_x]
        active_cell.visited = True

        stack = [active_cell]

        while stack:

            active_cell = stack[-1]

            possible_moves = self._get_unvisited_neighbors(
                active_cell, grid, width, height
            )

            if possible_moves:

                random.shuffle(possible_moves)
                next_cell, direction, opposite_direction = possible_moves.pop()

                # remove walls between current and next
                active_cell.remove_wall(direction)
                next_cell.remove_wall(opposite_direction)

                next_cell.visited = True
                stack.append(next_cell)

            else:
                stack.pop()
