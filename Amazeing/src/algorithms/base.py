from abc import ABC, abstractmethod
from src.maze.cell import Cell


class BaseAlgorithm(ABC):

    @abstractmethod
    def carve(self, grid: list[list[Cell]], start_at: tuple[int, int]) -> None:
        pass
