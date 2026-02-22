"""
Base solver class for Sudoku puzzles.

Provides abstract interface for all solver implementations.
"""

from abc import ABC, abstractmethod


class BaseSolver(ABC):
    """
    Abstract base class for Sudoku solvers.
    
    All solver implementations should inherit from this class
    and implement the required methods.
    """
    
    def __init__(self):
        """Initialize the solver."""
        self.solution_count = 0
        self.steps = 0
    
    @abstractmethod
    def solve(self, puzzle):
        """
        Solve the puzzle and return the solution.
        
        Args:
            puzzle: 9x9 2D list representing the puzzle
            
        Returns:
            list: Solved 9x9 2D list, or None if no solution exists
        """
        pass
    
    @abstractmethod
    def find_all_solutions(self, puzzle, limit=None):
        """
        Find all possible solutions for the puzzle.
        
        Args:
            puzzle: 9x9 2D list representing the puzzle
            limit: Maximum number of solutions to find (None for all)
            
        Returns:
            list: List of all solution puzzles
        """
        pass
    
    def get_stats(self):
        """
        Get statistics about the last solve operation.
        
        Returns:
            dict: Dictionary with statistics (steps, solution_count, etc.)
        """
        return {
            'steps': self.steps,
            'solution_count': self.solution_count
        }