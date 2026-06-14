from src.maze.cell import N, E, S, W


def render_maze(
    grid: list[list],
    entry: tuple[int, int],
    exit: tuple[int, int]
) -> str:

    height = len(grid)
    width = len(grid[0])

    output = ""

    # top border
    output += "+" + "---+" * width + "\n"

    for y in range(height):
        row_top = "|"
        row_bottom = "+"

        for x in range(width):
            cell = grid[y][x]

            # ----------------------
            # CELL CONTENT
            # ----------------------
            if (x, y) == entry:
                row_top += " S "
            elif (x, y) == exit:
                row_top += " E "
            else:
                row_top += "   "

            # ----------------------
            # EAST WALL
            # ----------------------
            if cell.has_wall(E):
                row_top += "|"
            else:
                row_top += " "

            # ----------------------
            # SOUTH WALL
            # ----------------------
            if cell.has_wall(S):
                row_bottom += "---+"
            else:
                row_bottom += "   +"

        output += row_top + "\n"
        output += row_bottom + "\n"

    return output