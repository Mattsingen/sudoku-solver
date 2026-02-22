"""
Demo script to test the RuleValidator.
Shows validation of various puzzles - valid, invalid, complete, and partial.
"""

from src.validators.rule_validator import RuleValidator
from src.utils.helpers import print_puzzle


def test_valid_partial_puzzle():
    """Test a valid partial puzzle."""
    print("=" * 50)
    print("TEST 1: Valid Partial Puzzle")
    print("=" * 50)
    
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print_puzzle(puzzle)
    
    validator = RuleValidator(puzzle)
    is_valid = validator.validate()
    
    print(f"Is valid? {is_valid}")
    print(f"Is complete? {validator.is_complete()}")
    if validator.get_errors():
        print("Errors:", validator.get_errors())
    print()


def test_complete_valid_puzzle():
    """Test a complete, valid puzzle."""
    print("=" * 50)
    print("TEST 2: Complete Valid Puzzle")
    print("=" * 50)
    
    puzzle = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    
    print_puzzle(puzzle)
    
    validator = RuleValidator(puzzle)
    is_valid = validator.validate()
    
    print(f"Is valid? {is_valid}")
    print(f"Is complete? {validator.is_complete()}")
    if validator.get_errors():
        print("Errors:", validator.get_errors())
    print()


def test_duplicate_in_row():
    """Test puzzle with duplicate in a row."""
    print("=" * 50)
    print("TEST 3: Invalid - Duplicate in Row")
    print("=" * 50)
    
    puzzle = [
        [5, 3, 5, 0, 7, 0, 0, 0, 0],  # Two 5's in row 0
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print_puzzle(puzzle)
    
    validator = RuleValidator(puzzle)
    is_valid = validator.validate()
    
    print(f"Is valid? {is_valid}")
    print(f"Errors: {validator.get_errors()}")
    print()


def test_duplicate_in_column():
    """Test puzzle with duplicate in a column."""
    print("=" * 50)
    print("TEST 4: Invalid - Duplicate in Column")
    print("=" * 50)
    
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [5, 9, 8, 0, 0, 0, 0, 6, 0],  # Another 5 in column 0
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print_puzzle(puzzle)
    
    validator = RuleValidator(puzzle)
    is_valid = validator.validate()
    
    print(f"Is valid? {is_valid}")
    print(f"Errors: {validator.get_errors()}")
    print()


def test_duplicate_in_box():
    """Test puzzle with duplicate in a 3x3 box."""
    print("=" * 50)
    print("TEST 5: Invalid - Duplicate in Box")
    print("=" * 50)
    
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 5, 0, 0, 0, 0, 6, 0],  # Another 5 in top-left box
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print_puzzle(puzzle)
    
    validator = RuleValidator(puzzle)
    is_valid = validator.validate()
    
    print(f"Is valid? {is_valid}")
    print(f"Errors: {validator.get_errors()}")
    print()


def test_invalid_value():
    """Test puzzle with invalid value."""
    print("=" * 50)
    print("TEST 6: Invalid - Out of Range Value")
    print("=" * 50)
    
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 10, 3, 0, 0, 1],  # 10 is invalid
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print_puzzle(puzzle)
    
    validator = RuleValidator(puzzle)
    is_valid = validator.validate()
    
    print(f"Is valid? {is_valid}")
    print(f"Errors: {validator.get_errors()}")
    print()


def main():
    print("\n" + "=" * 50)
    print("SUDOKU VALIDATOR DEMO")
    print("=" * 50 + "\n")
    
    test_valid_partial_puzzle()
    test_complete_valid_puzzle()
    test_duplicate_in_row()
    test_duplicate_in_column()
    test_duplicate_in_box()
    test_invalid_value()
    
    print("=" * 50)
    print("DEMO COMPLETE!")
    print("=" * 50)


if __name__ == "__main__":
    main()
