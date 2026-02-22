"""
Demonstration of the multi-row bug fix.

This test shows that the puzzle parser now correctly rejects
puzzles with more than 9 rows of data.
"""

from src.parsers.puzzle_parser import PuzzleParser


def test_valid_9_rows():
    """Test that a valid 9-row puzzle is accepted."""
    parser = PuzzleParser()
    puzzle = """
5 3 . . . 7 . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
"""
    result = parser.parse(puzzle)
    assert result is not None, f"Should accept 9 rows, but got error: {parser.errors}"
    print("PASS: Valid 9-row puzzle accepted")


def test_invalid_10_rows():
    """Test that a 10-row puzzle is rejected."""
    parser = PuzzleParser()
    puzzle = """
5 3 . . . 7 . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
1 2 3 4 5 6 7 8 9
"""
    result = parser.parse(puzzle)
    assert result is None, "Should reject 10 rows"
    assert any("too many rows" in str(e).lower() for e in parser.errors), \
        f"Should mention 'too many rows', but got: {parser.errors}"
    print("PASS: 10-row puzzle correctly rejected")
    print(f"  Error message: {parser.errors[0]}")


def test_with_separator_lines():
    """Test that separator lines don't count as puzzle rows."""
    parser = PuzzleParser()
    puzzle = """
5 3 . . . 7 . . .
6 . . 1 9 5 . . .
- - - - - - - - -
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
- - - - - - - - -
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
- - - - - - - - -
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
"""
    result = parser.parse(puzzle)
    assert result is not None, f"Should handle separator lines, but got: {parser.errors}"
    print("PASS: 9-row puzzle with separators accepted")


if __name__ == "__main__":
    print("Testing multi-row bug fix...\n")
    test_valid_9_rows()
    test_invalid_10_rows()
    test_with_separator_lines()
    print("\nAll tests passed! Bug fix verified.")
