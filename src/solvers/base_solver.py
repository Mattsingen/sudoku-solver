from abc import ABC, abstractmethod

class BaseSolver(ABC):
    @abstractmethod
    def solve(self, puzzle):
        pass

    @abstractmethod
    def validate(self, puzzle):
        pass