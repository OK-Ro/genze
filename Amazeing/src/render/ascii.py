"""Module handling the visual text-based rendering of the maze structure."""

from src.maze.generator import MazeGenerator


class AsciiRenderer:
    """Transforms a generated maze grid into an eye-readable ASCII art canvas."""

    def __init__(self, generator: MazeGenerator) -> None:
        """Initialize the renderer with a reference to the active generator."""
        self.generator = generator
        self.width = generator.width
        self.height = generator.height

    def render(self) -> str:
        """Converts cell states into a formatted ASCII wall string map."""
        if not self.generator.grid:
            return "Empty maze grid. Run generate() first."

        lines = []

        # Process the grid row-by-row
        for y in range(self.height):
            top_line = ""
            mid_line = ""

            for x in range(self.width):
                cell = self.generator.grid[y][x]

                # 1. Evaluate the ceiling (North wall)
                top_line += "+"
                top_line += "---" if cell.has_wall("N") else "   "

                # 2. Evaluate the side profile (West wall) and cavity space
                mid_line += "|" if cell.has_wall("W") else " "
                mid_line += "   "

            # Add structural right-side caps to close the row loop
            top_line += "+"
            mid_line += "|" if self.generator.grid[y][-1].has_wall("E") else " "
            
            lines.append(top_line)
            lines.append(mid_line)

        # 3. Formulate the final baseline floor boundary
        bottom_line = ""
        for x in range(self.width):
            bottom_line += "+"
            bottom_line += "---" if self.generator.grid[-1][x].has_wall("S") else "   "
        bottom_line += "+"
        lines.append(bottom_line)

        return "\n".join(lines)