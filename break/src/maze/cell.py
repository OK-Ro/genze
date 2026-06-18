class Cell:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.visited: bool = False

        self.walls: dict[str, bool] = {
            "N": True,
            "E": True,
            "S": True,
            "W": True,
        }

    def has_wall(self, direction: str) -> bool:
        direction = direction.upper()

        if direction not in self.walls:
            raise ValueError(
                f"[Cell.has_wall] Invalid direction '{direction}' at ({self.x},{self.y}). "
                f"Expected one of: N, E, S, W"
            )

        return self.walls[direction]

    def remove_wall(self, direction: str) -> None:
        direction = direction.upper()

        if direction not in self.walls:
            raise ValueError(
                f"[Cell.remove_wall] Invalid direction '{direction}' at ({self.x},{self.y}). "
                f"Expected one of: N, E, S, W"
            )

        self.walls[direction] = False

    def add_wall(self, direction: str) -> None:
        direction = direction.upper()

        if direction not in self.walls:
            raise ValueError(
                f"[Cell.add_wall] Invalid direction '{direction}' at ({self.x},{self.y}). "
                f"Expected one of: N, E, S, W"
            )

        self.walls[direction] = True

    def _convert_to_hex(self) -> str:
        value = 0

        if self.walls["N"]:
            value += 1
        if self.walls["E"]:
            value += 2
        if self.walls["S"]:
            value += 4
        if self.walls["W"]:
            value += 8

        return format(value, "X")