"""
Validator module for Sudoku puzzles.

This module provides validation for Sudoku puzzles to ensure they follow
standard Sudoku rules: no duplicates in rows, columns, or 3x3 boxes.
"""

from typing import Optional


class RuleValidator:
    """
    Validates Sudoku puzzles according to standard rules.
    
    Can validate both complete and partial puzzles. For partial puzzles,
    empty cells (represented by 0) are ignored during validation.
    """
    
    def __init__(self, puzzle: Optional[list[list[int]]] = None) -> None:
        """
        Initialize the validator with an optional puzzle.
        
        Args:
            puzzle: 9x9 2D list representing the puzzle (optional)
        """
        self.puzzle: Optional[list[list[int]]] = puzzle
        self.errors: list[str] = []
    
    def validate(self, puzzle: Optional[list[list[int]]] = None) -> bool:
        """
        Main validation method. Checks if puzzle follows all Sudoku rules.
        
        Args:
            puzzle: 9x9 2D list to validate (uses initialized puzzle if None)
            
        Returns:
            bool: True if puzzle is valid, False otherwise
        """
        if puzzle is not None:
            self.puzzle = puzzle
        
        if self.puzzle is None:
            self.errors.append("No puzzle provided for validation")
            return False
        
        self.errors = []
        
        # Check dimensions
        if not self._check_dimensions():
            return False
        
        # Check values are in valid range
        if not self._check_values():
            return False
        
        # Check Sudoku rules
        return (self.check_rows() and 
                self.check_columns() and 
                self.check_boxes())
    
    def _check_dimensions(self) -> bool:
        """Check if puzzle has correct 9x9 dimensions."""
        assert self.puzzle is not None
        if not isinstance(self.puzzle, list) or len(self.puzzle) != 9:
            self.errors.append("Puzzle must be a 9x9 grid")
            return False
        
        for i, row in enumerate(self.puzzle):
            if not isinstance(row, list) or len(row) != 9:
                self.errors.append(f"Row {i+1} does not have 9 columns")
                return False
        
        return True
    
    def _check_values(self) -> bool:
        """Check if all values are integers between 0-9."""
        assert self.puzzle is not None
        for i, row in enumerate(self.puzzle):
            for j, val in enumerate(row):
                if not isinstance(val, int) or val < 0 or val > 9:
                    self.errors.append(
                        f"Invalid value '{val}' at position (row {i+1}, col {j+1}). "
                        f"Must be integer 1-9 (or 0 for empty)"
                    )
                    return False
        return True
    
    def check_rows(self) -> bool:
        """
        Validate all rows for duplicate numbers.
        
        Returns:
            bool: True if all rows are valid, False otherwise
        """
        assert self.puzzle is not None
        for i, row in enumerate(self.puzzle):
            if not self._is_unique(row):
                duplicates = self._find_duplicates(row)
                self.errors.append(
                    f"Row {i+1} contains duplicate(s): {duplicates}"
                )
                return False
        return True
    
    def check_columns(self) -> bool:
        """
        Validate all columns for duplicate numbers.
        
        Returns:
            bool: True if all columns are valid, False otherwise
        """
        assert self.puzzle is not None
        for col_idx in range(9):
            column = [self.puzzle[row_idx][col_idx] for row_idx in range(9)]
            if not self._is_unique(column):
                duplicates = self._find_duplicates(column)
                self.errors.append(
                    f"Column {col_idx+1} contains duplicate(s): {duplicates}"
                )
                return False
        return True
    
    def check_boxes(self) -> bool:
        """
        Validate all 3x3 boxes for duplicate numbers.
        
        Returns:
            bool: True if all boxes are valid, False otherwise
        """
        assert self.puzzle is not None
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = self._get_box(box_row, box_col)
                if not self._is_unique(box):
                    duplicates = self._find_duplicates(box)
                    box_num = (box_row // 3) * 3 + (box_col // 3) + 1
                    self.errors.append(
                        f"Box {box_num} (rows {box_row+1}-{box_row+3}, "
                        f"cols {box_col+1}-{box_col+3}) contains duplicate(s): {duplicates}"
                    )
                    return False
        return True
    
    def _get_box(self, start_row: int, start_col: int) -> list[int]:
        """
        Extract all values from a 3x3 box.
        
        Args:
            start_row: Starting row index of the box
            start_col: Starting column index of the box
            
        Returns:
            list: Flat list of 9 values from the box
        """
        assert self.puzzle is not None
        box: list[int] = []
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                box.append(self.puzzle[i][j])
        return box
    
    def _is_unique(self, values: list[int]) -> bool:
        """
        Check if non-zero values in a list are unique.
        
        Args:
            values: List of integers
            
        Returns:
            bool: True if no duplicates exist (ignoring zeros)
        """
        non_zero_values = [v for v in values if v != 0]
        return len(non_zero_values) == len(set(non_zero_values))
    
    def _find_duplicates(self, values: list[int]) -> list[int]:
        """
        Find duplicate non-zero values in a list.
        
        Args:
            values: List of integers
            
        Returns:
            list: Sorted list of duplicate values
        """
        non_zero_values = [v for v in values if v != 0]
        seen: set[int] = set()
        duplicates: set[int] = set()
        for v in non_zero_values:
            if v in seen:
                duplicates.add(v)
            seen.add(v)
        return sorted(duplicates)
    
    def is_complete(self) -> bool:
        """
        Check if puzzle is completely filled (no zeros).
        
        Returns:
            bool: True if no empty cells, False otherwise
        """
        if self.puzzle is None:
            return False
        
        for row in self.puzzle:
            if 0 in row:
                return False
        return True
    
    def get_errors(self) -> list[str]:
        """
        Get list of validation errors from last validation.
        
        Returns:
            list: List of error message strings
        """
        return self.errors.copy()
    
    # Legacy method names for backward compatibility
    def is_valid(self) -> bool:
        """Legacy method - use validate() instead."""
        return self.validate()
    
    def check_subgrids(self) -> bool:
        """Legacy method - use check_boxes() instead."""
        return self.check_boxes()