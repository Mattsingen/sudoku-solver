from flask import Flask, render_template, request, jsonify
from src.solvers.regular_solver import RegularSolver
from src.solvers.variant_solver import VariantSolver
from src.parsers.puzzle_parser import PuzzleParser
from src.validators.rule_validator import RuleValidator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    puzzle_data = request.json.get('puzzle')
    puzzle_type = request.json.get('type')

    parser = PuzzleParser()
    puzzle = parser.parse(puzzle_data)

    validator = RuleValidator()
    if not validator.validate(puzzle):
        return jsonify({'error': 'Invalid puzzle'}), 400

    solver = RegularSolver() if puzzle_type == 'regular' else VariantSolver()
    solution = solver.solve(puzzle)

    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(debug=True)