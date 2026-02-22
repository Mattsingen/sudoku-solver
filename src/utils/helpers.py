"""
Helper utilities for Sudoku puzzle operations.

This module provides utility functions for creating, manipulating,
and displaying Sudoku puzzles.
"""

import copy


def create_empty_puzzle():
    """
    Create an empty 9x9 Sudoku puzzle filled with zeros.
    
    Returns:
        list: A 9x9 2D list filled with zeros
    """
    return [[0 for _ in range(9)] for _ in range(9)]


def is_valid_puzzle(puzzle):
    """
    Check if a puzzle has valid dimensions (9x9).
    
    Args:
        puzzle: The puzzle to validate
        
    Returns:
        bool: True if puzzle is 9x9, False otherwise
    """
    if not isinstance(puzzle, list) or len(puzzle) != 9:
        return False
    for row in puzzle:
        if not isinstance(row, list) or len(row) != 9:
            return False
    return True


def copy_puzzle(puzzle):
    """
    Create a deep copy of a puzzle.
    
    Args:
        puzzle: The puzzle to copy
        
    Returns:
        list: A deep copy of the puzzle
    """
    return copy.deepcopy(puzzle)


def get_empty_cells(puzzle):
    """
    Find all empty cells (with value 0) in the puzzle.
    
    Args:
        puzzle: The puzzle to search
        
    Returns:
        list: List of (row, col) tuples for empty cells
    """
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells


def find_empty_location(puzzle):
    """
    Find the first empty location (with value 0) in the puzzle.
    
    Args:
        puzzle: The puzzle to search
        
    Returns:
        tuple: (row, col) of first empty cell, or None if no empty cells
    """
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return (i, j)
    return None


def is_valid_move(puzzle, row, col, num):
    """
    Check if placing a number at a specific position is valid.
    
    Validates that the number doesn't already exist in:
    - The same row
    - The same column
    - The same 3x3 box
    
    Args:
        puzzle: The puzzle to check
        row: Row index (0-8)
        col: Column index (0-8)
        num: Number to place (1-9)
        
    Returns:
        bool: True if move is valid, False otherwise
    """
    # Check row and column
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False
    
    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if puzzle[i][j] == num:
                return False
    
    return True


def print_puzzle(puzzle):
    """
    Print the puzzle in a formatted, readable way with box separators.
    
    Args:
        puzzle: The puzzle to print
    """
    print("\n" + "─" * 25)
    for i, row in enumerate(puzzle):
        if i > 0 and i % 3 == 0:
            print("├" + "───────┼───────┼───────┤")
        
        row_str = "│ "
        for j, cell in enumerate(row):
            if j > 0 and j % 3 == 0:
                row_str += "│ "
            row_str += str(cell) if cell != 0 else "·"
            row_str += " "
        row_str += "│"
        print(row_str)
    print("─" * 25 + "\n")


def format_puzzle(puzzle):
    """
    Format the puzzle as a simple string representation.
    
    Args:
        puzzle: The puzzle to format
        
    Returns:
        str: String representation with dots for empty cells
    """
    return "\n".join(" ".join(str(cell) if cell != 0 else '.' for cell in row) for row in puzzle)


# Backward compatibility aliases
format_board = format_puzzle
print_board = print_puzzle