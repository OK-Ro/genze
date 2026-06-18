from abc import ABC, abstractmethod
from src.maze.cell import Cell


class MazeAlgorithms(ABC):

    @abstractmethod
    def carve(self, grid: list[list[Cell]], start_At: tuple[int, int], width:int, height:int) -> None:
        pass
