"""
Demo script to test the PuzzleParser.
Shows parsing of various input formats.
"""

from src.parsers.puzzle_parser import PuzzleParser
from src.utils.helpers import print_puzzle


def test_single_line_format():
    """Test parsing a single line 81-character string."""
    print("=" * 60)
    print("TEST 1: Single Line Format (81 characters)")
    print("=" * 60)
    
    puzzle_string = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
    print(f"Input: {puzzle_string}\n")
    
    parser = PuzzleParser()
    puzzle = parser.parse(puzzle_string)
    
    if puzzle:
        print("✓ Parsing successful!")
        print_puzzle(puzzle)
    else:
        print("✗ Parsing failed!")
        print(f"Errors: {parser.get_errors()}")
    print()


def test_single_line_with_dots():
    """Test parsing with dots for empty cells."""
    print("=" * 60)
    print("TEST 2: Single Line with Dots for Empty Cells")
    print("=" * 60)
    
    puzzle_string = "53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
    print(f"Input: {puzzle_string}\n")
    
    parser = PuzzleParser()
    puzzle = parser.parse(puzzle_string)
    
    if puzzle:
        print("✓ Parsing successful!")
        print_puzzle(puzzle)
    else:
        print("✗ Parsing failed!")
        print(f"Errors: {parser.get_errors()}")
    print()


def test_multiline_format():
    """Test parsing multi-line format."""
    print("=" * 60)
    print("TEST 3: Multi-Line Format")
    print("=" * 60)
    
    puzzle_string = """5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9"""
    
    print("Input:")
    print(puzzle_string)
    print()
    
    parser = PuzzleParser()
    puzzle = parser.parse(puzzle_string)
    
    if puzzle:
        print("✓ Parsing successful!")
        print_puzzle(puzzle)
    else:
        print("✗ Parsing failed!")
        print(f"Errors: {parser.get_errors()}")
    print()


def test_grid_format_with_separators():
    """Test parsing grid format with separator lines."""
    print("=" * 60)
    print("TEST 4: Grid Format with Separators")
    print("=" * 60)
    
    puzzle_string = """─────────────────────────
│ 5 3 · │ · 7 · │ · · · │
│ 6 · · │ 1 9 5 │ · · · │
│ · 9 8 │ · · · │ · 6 · │
├───────┼───────┼───────┤
│ 8 · · │ · 6 · │ · · 3 │
│ 4 · · │ 8 · 3 │ · · 1 │
│ 7 · · │ · 2 · │ · · 6 │
├───────┼───────┼───────┤
│ · 6 · │ · · · │ 2 8 · │
│ · · · │ 4 1 9 │ · · 5 │
│ · · · │ · 8 · │ · 7 9 │
─────────────────────────"""
    
    print("Input:")
    print(puzzle_string)
    print()
    
    parser = PuzzleParser()
    puzzle = parser.parse(puzzle_string)
    
    if puzzle:
        print("✓ Parsing successful!")
        print_puzzle(puzzle)
    else:
        print("✗ Parsing failed!")
        print(f"Errors: {parser.get_errors()}")
    print()


def test_list_format():
    """Test parsing from a 2D list."""
    print("=" * 60)
    print("TEST 5: 2D List Format")
    print("=" * 60)
    
    puzzle_list = [
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
    
    print("Input: 2D list (9x9)\n")
    
    parser = PuzzleParser()
    puzzle = parser.parse(puzzle_list)
    
    if puzzle:
        print("✓ Parsing successful!")
        print_puzzle(puzzle)
    else:
        print("✗ Parsing failed!")
        print(f"Errors: {parser.get_errors()}")
    print()


def test_json_format():
    """Test parsing from JSON string."""
    print("=" * 60)
    print("TEST 6: JSON Format")
    print("=" * 60)
    
    puzzle_json = """{
        "puzzle": [
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
    }"""
    
    print("Input: JSON string\n")
    
    parser = PuzzleParser()
    puzzle = parser.parse(puzzle_json)
    
    if puzzle:
        print("✓ Parsing successful!")
        print_puzzle(puzzle)
    else:
        print("✗ Parsing failed!")
        print(f"Errors: {parser.get_errors()}")
    print()


def test_invalid_input():
    """Test parsing invalid input."""
    print("=" * 60)
    print("TEST 7: Invalid Input (Too Short)")
    print("=" * 60)
    
    puzzle_string = "53007000060019500009800006"  # Only 27 chars
    print(f"Input: {puzzle_string} (too short)\n")
    
    parser = PuzzleParser()
    puzzle = parser.parse(puzzle_string)
    
    if puzzle:
        print("✓ Parsing successful!")
        print_puzzle(puzzle)
    else:
        print("✗ Parsing failed (as expected)")
        print(f"Errors: {parser.get_errors()}")
    print()


def test_output_formats():
    """Test converting puzzle to different output formats."""
    print("=" * 60)
    print("TEST 8: Output Format Conversion")
    print("=" * 60)
    
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
    
    parser = PuzzleParser()
    
    print("Single Line Format:")
    print(parser.to_string(puzzle, format='line'))
    print()
    
    print("Simple Format:")
    print(parser.to_string(puzzle, format='simple'))
    print()
    
    print("Grid Format:")
    print(parser.to_string(puzzle, format='grid'))
    print()


def main():
    print("\n" + "=" * 60)
    print("SUDOKU PARSER DEMO")
    print("=" * 60 + "\n")
    
    test_single_line_format()
    test_single_line_with_dots()
    test_multiline_format()
    test_grid_format_with_separators()
    test_list_format()
    test_json_format()
    test_invalid_input()
    test_output_formats()
    
    print("=" * 60)
    print("DEMO COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    main()
