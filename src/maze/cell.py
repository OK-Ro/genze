from dataclasses import dataclass

# Wall directions (bit meaning from the subject)
# 0 -> North
# 1 -> East
# 2 -> South
# 3 -> West

N, E, S, W = "N", "E", "S", "W"


@dataclass
class Cell:
    # Each side of the cell has a wall (True = wall exists)
    north: bool = True
    east: bool = True
    south: bool = True
    west: bool = True

    def has_wall(self, direction: str) -> bool:
        """Check if a wall exists in the given direction."""
        if direction == N:
            return self.north
        if direction == E:
            return self.east
        if direction == S:
            return self.south
        if direction == W:
            return self.west
        return False

    def remove_wall(self, direction: str) -> None:
        """Remove a wall (open passage) in a direction."""
        if direction == N:
            self.north = False
        elif direction == E:
            self.east = False
        elif direction == S:
            self.south = False
        elif direction == W:
            self.west = False

    def add_wall(self, direction: str) -> None:
        """Add a wall (close passage) in a direction."""
        if direction == N:
            self.north = True
        elif direction == E:
            self.east = True
        elif direction == S:
            self.south = True
        elif direction == W:
            self.west = True

    def to_hex(self) -> str:
        """
        Convert walls into a hexadecimal value.

        Bit layout (IMPORTANT for project):
        - North = 1 (0001)
        - East  = 2 (0010)
        - South = 4 (0100)
        - West  = 8 (1000)

        Example:
        walls = North + South closed → 1 + 4 = 5 → "5"
        """
        value = 0

        if self.north:
            value += 1   # bit 0
        if self.east:
            value += 2   # bit 1
        if self.south:
            value += 4   # bit 2
        if self.west:
            value += 8   # bit 3

        return format(value, "x")