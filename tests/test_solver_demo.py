"""
Demo script to test the RegularSolver.
Shows solving capabilities with various difficulty puzzles.
"""

from src.solvers.regular_solver import RegularSolver
from src.utils.helpers import print_puzzle
import time


def test_easy_puzzle():
    """Test solving an easy puzzle."""
    print("=" * 60)
    print("TEST 1: Easy Puzzle")
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
    
    print("Original Puzzle:")
    print_puzzle(puzzle)
    
    solver = RegularSolver()
    start_time = time.time()
    solution = solver.solve(puzzle)
    solve_time = time.time() - start_time
    
    if solution:
        print("✓ Solution Found!")
        print_puzzle(solution)
        stats = solver.get_stats()
        print(f"Solving took {solve_time*1000:.2f}ms")
        print(f"Steps: {stats['steps']}")
    else:
        print("✗ No solution found")
    print()


def test_medium_puzzle():
    """Test solving a medium difficulty puzzle."""
    print("=" * 60)
    print("TEST 2: Medium Puzzle")
    print("=" * 60)
    
    puzzle = [
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 6, 0, 4, 5],
        [0, 4, 0, 2, 0, 0, 0, 6, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0, 0]
    ]
    
    print("Original Puzzle:")
    print_puzzle(puzzle)
    
    solver = RegularSolver()
    start_time = time.time()
    solution = solver.solve(puzzle)
    solve_time = time.time() - start_time
    
    if solution:
        print("✓ Solution Found!")
        print_puzzle(solution)
        stats = solver.get_stats()
        print(f"Solving took {solve_time*1000:.2f}ms")
        print(f"Steps: {stats['steps']}")
    else:
        print("✗ No solution found")
    print()


def test_hard_puzzle():
    """Test solving a hard puzzle."""
    print("=" * 60)
    print("TEST 3: Hard Puzzle (Minimal Clues)")
    print("=" * 60)
    
    puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9]
    ]
    
    print("Original Puzzle:")
    print_puzzle(puzzle)
    
    solver = RegularSolver()
    start_time = time.time()
    solution = solver.solve(puzzle)
    solve_time = time.time() - start_time
    
    if solution:
        print("✓ Solution Found!")
        print_puzzle(solution)
        stats = solver.get_stats()
        print(f"Solving took {solve_time*1000:.2f}ms")
        print(f"Steps: {stats['steps']}")
    else:
        print("✗ No solution found")
    print()


def test_invalid_puzzle():
    """Test with an invalid puzzle (no solution)."""
    print("=" * 60)
    print("TEST 4: Invalid Puzzle (No Solution)")
    print("=" * 60)
    
    puzzle = [
        [5, 5, 0, 0, 7, 0, 0, 0, 0],  # Two 5's in first row
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("Original Puzzle (Invalid):")
    print_puzzle(puzzle)
    
    solver = RegularSolver()
    start_time = time.time()
    solution = solver.solve(puzzle)
    solve_time = time.time() - start_time
    
    if solution:
        print("✓ Solution Found!")
        print_puzzle(solution)
    else:
        print("✗ No solution found (as expected - puzzle has duplicate 5's in row 1)")
        print(f"Validation failed in {solve_time*1000:.2f}ms")
    print()


def test_multiple_solutions():
    """Test puzzle with multiple solutions."""
    print("=" * 60)
    print("TEST 5: Multiple Solutions")
    print("=" * 60)
    
    # A puzzle with very few clues may have multiple solutions
    puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    print("Empty Puzzle (with one clue):")
    print_puzzle(puzzle)
    
    solver = RegularSolver()
    
    print("Finding first solution...")
    solution = solver.solve(puzzle)
    if solution:
        print("First solution:")
        print_puzzle(solution)
    
    print("Checking if solution is unique...")
    is_unique = solver.has_unique_solution(puzzle)
    print(f"Has unique solution? {is_unique}")
    
    print("\nFinding multiple solutions (limit 5)...")
    solutions = solver.find_all_solutions(puzzle, limit=5)
    print(f"Found {len(solutions)} solutions")
    
    if len(solutions) > 1:
        print("\nSecond solution:")
        print_puzzle(solutions[1])
    print()


def test_unique_solution():
    """Test checking for unique solution."""
    print("=" * 60)
    print("TEST 6: Unique Solution Check")
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
    
    print("Original Puzzle:")
    print_puzzle(puzzle)
    
    solver = RegularSolver()
    
    print("Checking for unique solution...")
    start_time = time.time()
    is_unique = solver.has_unique_solution(puzzle)
    check_time = time.time() - start_time
    
    print(f"Has unique solution? {is_unique}")
    print(f"Check took {check_time*1000:.2f}ms")
    stats = solver.get_stats()
    print(f"Steps: {stats['steps']}")
    print()


def main():
    print("\n" + "=" * 60)
    print("SUDOKU SOLVER DEMO")
    print("=" * 60 + "\n")
    
    test_easy_puzzle()
    test_medium_puzzle()
    test_hard_puzzle()
    test_invalid_puzzle()
    test_multiple_solutions()
    test_unique_solution()
    
    print("=" * 60)
    print("DEMO COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    main()
