"""
Variant Sudoku solver.

Currently falls back to the regular solver until variant rules are implemented.
"""

from src.solvers.base_solver import BaseSolver
from src.solvers.regular_solver import RegularSolver
from src.validators.rule_validator import RuleValidator


class VariantSolver(BaseSolver):
    def __init__(self):
        super().__init__()
        self.validator = RuleValidator()
        self.regular_solver = RegularSolver()

    def solve(self, puzzle):
        return self.regular_solver.solve(puzzle)

    def find_all_solutions(self, puzzle, limit=None):
        return self.regular_solver.find_all_solutions(puzzle, limit=limit)

    def validate(self, puzzle):
        return self.validator.validate(puzzle)