"""
Demo script to test the helper functions.
Run this to see the helpers in action!
"""

from src.utils.helpers import (
    create_empty_puzzle,
    is_valid_puzzle,
    print_puzzle,
    is_valid_move,
    find_empty_location,
    get_empty_cells
)


def main():
    print("=== Sudoku Solver - Helper Functions Demo ===\n")
    
    # Create an empty puzzle
    print("1. Creating an empty puzzle:")
    puzzle = create_empty_puzzle()
    print_puzzle(puzzle)
    
    # Validate puzzle dimensions
    print("2. Validating puzzle dimensions:")
    print(f"   Is valid 9x9 puzzle? {is_valid_puzzle(puzzle)}")
    
    # Add some numbers to create a sample puzzle
    print("\n3. Creating a sample puzzle with some numbers:")
    sample_puzzle = [
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
    print_puzzle(sample_puzzle)
    
    # Find empty location
    print("4. Finding first empty location:")
    empty_loc = find_empty_location(sample_puzzle)
    if empty_loc is not None:
        print(f"   First empty cell at: row {empty_loc[0]}, col {empty_loc[1]}")
    else:
        print("   No empty cells found")
    
    # Count empty cells
    print("\n5. Counting all empty cells:")
    empty_cells = get_empty_cells(sample_puzzle)
    print(f"   Total empty cells: {len(empty_cells)}")
    print(f"   First 5 empty positions: {empty_cells[:5]}")
    
    # Test valid move
    print("\n6. Testing if placing '2' at position (0, 2) is valid:")
    row, col, num = 0, 2, 2
    is_valid = is_valid_move(sample_puzzle, row, col, num)
    print(f"   Can place {num} at ({row}, {col})? {is_valid}")
    
    # Test invalid move
    print("\n7. Testing if placing '5' at position (0, 2) is valid:")
    row, col, num = 0, 2, 5
    is_valid = is_valid_move(sample_puzzle, row, col, num)
    print(f"   Can place {num} at ({row}, {col})? {is_valid} (should be False - 5 already in row)")
    
    print("\n=== Demo Complete! ===")


if __name__ == "__main__":
    main()
