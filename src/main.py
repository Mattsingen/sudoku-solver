# Entry point of the Sudoku solver application

from solvers.regular_solver import RegularSolver
from solvers.variant_solver import VariantSolver
from parsers.puzzle_parser import PuzzleParser
from validators.rule_validator import RuleValidator

def main():
    print("Welcome to the Sudoku Solver!")
    puzzle_input = input("Please enter your Sudoku puzzle (in a supported format): ")
    
    parser = PuzzleParser()
    puzzle = parser.parse(puzzle_input)
    
    validator = RuleValidator()
    if not validator.validate(puzzle):
        print("The provided puzzle is invalid.")
        return
    
    solver_type = input("Select solver type (regular/variant): ").strip().lower()
    
    if solver_type == 'regular':
        solver = RegularSolver()
    elif solver_type == 'variant':
        solver = VariantSolver()
    else:
        print("Invalid solver type selected.")
        return
    
    solution = solver.solve(puzzle)
    
    if solution:
        print("Solved Puzzle:")
        print(solution)
    else:
        print("No solution found for the provided puzzle.")

if __name__ == "__main__":
    main()