class RuleValidator:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def is_valid(self):
        return self.check_rows() and self.check_columns() and self.check_subgrids()

    def check_rows(self):
        for row in self.puzzle:
            if not self.is_unique(row):
                return False
        return True

    def check_columns(self):
        for col in range(len(self.puzzle)):
            column = [self.puzzle[row][col] for row in range(len(self.puzzle))]
            if not self.is_unique(column):
                return False
        return True

    def check_subgrids(self):
        size = int(len(self.puzzle) ** 0.5)
        for row in range(0, len(self.puzzle), size):
            for col in range(0, len(self.puzzle), size):
                subgrid = [self.puzzle[r][c] for r in range(row, row + size) for c in range(col, col + size)]
                if not self.is_unique(subgrid):
                    return False
        return True

    def is_unique(self, values):
        values = [v for v in values if v != 0]  # Assuming 0 represents an empty cell
        return len(values) == len(set(values))