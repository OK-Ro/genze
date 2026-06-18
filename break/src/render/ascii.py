from src.maze.generator import MazeGenerator


class MazeRenderer:
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    WALL = "██"
    EMPTY = "  "
    PATH = "▓▓"   # stable visual block (prevents spacing issues)

    def __init__(self, generator: MazeGenerator):
        self.generator = generator
        self.grid = generator.grid
        self.width = generator.width
        self.height = generator.height
        self.entry = generator.entry
        self.exit = generator.exit

    def block_render(self, path: list[tuple[int, int]] | None = None) -> str:
        grid = self.grid

        if not grid:
            return "Empty maze grid. Run generate() first."

        output = []

        # =========================
        # TOP BORDER
        # =========================
        output.append(self.WALL * (self.width * 2 + 1))

        path_set = set(path) if path else set()

        for y in range(self.height):

            line = self.WALL

            for x in range(self.width):
                cell = grid[y][x]

                # -------------------------
                # START / EXIT / PATH
                # -------------------------
                if (x, y) == self.entry:
                    cell_block = f"{self.GREEN}{self.WALL}{self.RESET}"

                elif (x, y) == self.exit:
                    cell_block = f"{self.RED}{self.WALL}{self.RESET}"

                elif (x, y) in path_set:
                    cell_block = f"{self.BLUE}{self.PATH}{self.RESET}"

                else:
                    cell_block = self.EMPTY

                line += cell_block

                # EAST WALL
                line += self.WALL if cell.has_wall("E") else self.EMPTY

            output.append(line)

            # -------------------------
            # SOUTH WALL LINE
            # -------------------------
            line = self.WALL

            for x in range(self.width):
                cell = grid[y][x]

                line += self.WALL if cell.has_wall("S") else self.EMPTY
                line += self.WALL

            output.append(line)

        return "\n".join(output)