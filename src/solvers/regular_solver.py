"""
Standard Sudoku solver using backtracking algorithm.

This module implements a classic backtracking algorithm to solve
standard 9x9 Sudoku puzzles.
"""

from src.solvers.base_solver import BaseSolver
from src.utils.helpers import copy_puzzle, find_empty_location, is_valid_move
from src.validators.rule_validator import RuleValidator


class RegularSolver(BaseSolver):
    """
    Solves standard 9x9 Sudoku puzzles using backtracking.
    
    The backtracking algorithm:
    1. Find an empty cell
    2. Try numbers 1-9 in that cell
    3. For each valid number, recursively try to solve the rest
    4. If stuck, backtrack and try the next number
    5. Return solution when puzzle is complete
    """
    
    def __init__(self):
        """Initialize the solver."""
        super().__init__()
        self.validator = RuleValidator()
    
    def solve(self, puzzle):
        """
        Solve the puzzle using backtracking algorithm.
        
        Args:
            puzzle: 9x9 2D list representing the puzzle
            
        Returns:
            list: Solved puzzle, or None if no solution exists
        """
        # Reset statistics
        self.steps = 0
        self.solution_count = 0
        
        # Validate input puzzle
        if not self.validator.validate(puzzle):
            return None
        
        # Make a copy to avoid modifying the original
        puzzle_copy = copy_puzzle(puzzle)
        
        # Solve using backtracking
        if self._backtrack(puzzle_copy):
            self.solution_count = 1
            return puzzle_copy
        
        return None
    
    def find_all_solutions(self, puzzle, limit=None):
        """
        Find all possible solutions for the puzzle.
        
        Args:
            puzzle: 9x9 2D list representing the puzzle
            limit: Maximum number of solutions to find (None for all)
            
        Returns:
            list: List of all solution puzzles
        """
        # Reset statistics
        self.steps = 0
        self.solution_count = 0
        
        # Validate input puzzle
        if not self.validator.validate(puzzle):
            return []
        
        # Make a copy to avoid modifying the original
        puzzle_copy = copy_puzzle(puzzle)
        
        # Find all solutions
        solutions = []
        self._find_all_solutions(puzzle_copy, solutions, limit)
        
        self.solution_count = len(solutions)
        return solutions
    
    def _backtrack(self, puzzle):
        """
        Recursive backtracking algorithm to solve the puzzle.
        
        Args:
            puzzle: Current puzzle state (modified in place)
            
        Returns:
            bool: True if solution found, False otherwise
        """
        self.steps += 1
        
        # Find next empty location
        empty = find_empty_location(puzzle)
        
        # If no empty location, puzzle is solved
        if empty is None:
            return True
        
        row, col = empty
        
        # Try numbers 1 through 9
        for num in range(1, 10):
            if is_valid_move(puzzle, row, col, num):
                # Place the number
                puzzle[row][col] = num
                
                # Recursively try to solve the rest
                if self._backtrack(puzzle):
                    return True
                
                # If that didn't work, backtrack
                puzzle[row][col] = 0
        
        # No valid number found, backtrack
        return False
    
    def _find_all_solutions(self, puzzle, solutions, limit):
        """
        Recursive algorithm to find all solutions.
        
        Args:
            puzzle: Current puzzle state (modified in place)
            solutions: List to accumulate solutions
            limit: Maximum number of solutions to find
        """
        self.steps += 1
        
        # Check if we've reached the limit
        if limit is not None and len(solutions) >= limit:
            return
        
        # Find next empty location
        empty = find_empty_location(puzzle)
        
        # If no empty location, we found a solution
        if empty is None:
            solutions.append(copy_puzzle(puzzle))
            return
        
        row, col = empty
        
        # Try numbers 1 through 9
        for num in range(1, 10):
            if is_valid_move(puzzle, row, col, num):
                # Place the number
                puzzle[row][col] = num
                
                # Recursively find more solutions
                self._find_all_solutions(puzzle, solutions, limit)
                
                # Backtrack to find other solutions
                puzzle[row][col] = 0
    
    def has_unique_solution(self, puzzle):
        """
        Check if the puzzle has exactly one unique solution.
        
        Args:
            puzzle: 9x9 2D list representing the puzzle
            
        Returns:
            bool: True if puzzle has exactly one solution
        """
        solutions = self.find_all_solutions(puzzle, limit=2)
        return len(solutions) == 1
    
    def count_solutions(self, puzzle, limit=100):
        """
        Count the number of solutions (up to limit).
        
        Args:
            puzzle: 9x9 2D list representing the puzzle
            limit: Maximum number of solutions to count
            
        Returns:
            int: Number of solutions found (capped at limit)
        """
        solutions = self.find_all_solutions(puzzle, limit=limit)
        return len(solutions)