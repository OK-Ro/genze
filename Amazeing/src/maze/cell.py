"""Module defining the structural Cell object for the maze grid matrix."""


class Cell:
    """Represents a single structural unit within the maze grid matrix.

    Tracks grid coordinates, algorithmic visitation state, and manages structural
    wall modifications across the four cardinal directions.
    """

    def __init__(self, x: int, y: int) -> None:
        """Initialize a standard maze cell with all four walls standing."""
        self.x: int = x
        self.y: int = y
        self.visited: bool = False

        self.walls: dict[str, bool] = {
            "N": True,
            "E": True,
            "S": True,
            "W": True
        }

    def has_wall(self, direction: str) -> bool:
        """Check if a specific wall is currently standing.

        Args:
            direction: A string flag ('N', 'E', 'S', or 'W').

        Returns:
            True if the wall exists, False if it has been carved out.
        """
   
        direct = direction.upper()
        if direct in self.walls:
            return self.walls[direct]
        raise ValueError(f"Invalid direction format: '{direction}'. Expected N, E, S, or W.")

    def remove_wall(self, direction: str) -> None:
        """Carve out a passage door by flattening a standing wall boundary."""
        direct = direction.upper()
        if direct in self.walls:
            self.walls[direct] = False
        else:
            raise ValueError(f"Invalid direction format: '{direction}'. Expected N, E, S, or W.")

    def add_wall(self, direction: str) -> None:
        """Build or restore a standing wall boundary blocking movement."""
        direct = direction.upper()
        if direct in self.walls:
            self.walls[direct] = True
        else:
            raise ValueError(f"Invalid direction format: '{direction}'. Expected N, E, S, or W.")

    def to_hex(self) -> str:
        """Translates the current four-wall active bits into a single hex digit string."""
        value = 0
        if self.walls["N"]: value += 1  # Bit 0
        if self.walls["E"]: value += 2  # Bit 1
        if self.walls["S"]: value += 4  # Bit 2
        if self.walls["W"]: value += 8  # Bit 3
        return format(value, 'X')