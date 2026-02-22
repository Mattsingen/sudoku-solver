"""
Flask web application for the Sudoku Solver.

Provides a user-friendly web interface for solving Sudoku puzzles.
"""

import sys
import os
import time

# Add parent directory to path so we can import src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify
from src.solvers.regular_solver import RegularSolver
from src.parsers.puzzle_parser import PuzzleParser
from src.validators.rule_validator import RuleValidator

app = Flask(__name__, template_folder='templates', static_folder='static')

# Configure max file size
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/solve', methods=['POST'])
def solve():
    """
    Solve a Sudoku puzzle.
    
    Expected JSON:
    {
        "puzzle": "puzzle string or 2D array",
        "format": "auto|line|multiline|json|list"
    }
    
    Returns:
    {
        "success": bool,
        "solution": solved puzzle,
        "time_ms": solving time,
        "steps": number of solver steps,
        "errors": validation errors
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'puzzle' not in data:
            return jsonify({
                'success': False,
                'errors': ['No puzzle provided']
            }), 400
        
        puzzle_input = data.get('puzzle')
        
        # Parse the puzzle
        parser = PuzzleParser()
        puzzle = parser.parse(puzzle_input)
        
        if puzzle is None:
            return jsonify({
                'success': False,
                'errors': parser.get_errors()
            }), 400
        
        # Validate the puzzle
        validator = RuleValidator(puzzle)
        if not validator.validate():
            return jsonify({
                'success': False,
                'errors': validator.get_errors()
            }), 400
        
        # Solve the puzzle
        solver = RegularSolver()
        start_time = time.time()
        solution = solver.solve(puzzle)
        elapsed_time = time.time() - start_time
        
        if solution is None:
            return jsonify({
                'success': False,
                'errors': ['No solution found for this puzzle']
            }), 400
        
        return jsonify({
            'success': True,
            'solution': solution,
            'time_ms': round(elapsed_time * 1000, 2),
            'steps': solver.steps
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'errors': [f'Server error: {str(e)}']
        }), 500


@app.route('/api/validate', methods=['POST'])
def validate():
    """
    Validate a Sudoku puzzle.
    
    Expected JSON:
    {
        "puzzle": "puzzle string or 2D array"
    }
    
    Returns:
    {
        "valid": bool,
        "complete": bool,
        "errors": validation errors
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'puzzle' not in data:
            return jsonify({
                'valid': False,
                'errors': ['No puzzle provided']
            }), 400
        
        puzzle_input = data.get('puzzle')
        
        # Parse the puzzle
        parser = PuzzleParser()
        puzzle = parser.parse(puzzle_input)
        
        if puzzle is None:
            return jsonify({
                'valid': False,
                'errors': parser.get_errors()
            }), 400
        
        # Validate the puzzle
        validator = RuleValidator(puzzle)
        is_valid = validator.validate()
        is_complete = validator.is_complete()
        
        return jsonify({
            'valid': is_valid,
            'complete': is_complete,
            'errors': validator.get_errors() if not is_valid else []
        })
    
    except Exception as e:
        return jsonify({
            'valid': False,
            'errors': [f'Server error: {str(e)}']
        }), 500


@app.route('/api/format', methods=['POST'])
def format_puzzle():
    """
    Format a puzzle for display.
    
    Expected JSON:
    {
        "puzzle": puzzle (2D array),
        "format": "grid|simple|line"
    }
    
    Returns:
    {
        "formatted": formatted string
    }
    """
    try:
        data = request.get_json()
        puzzle = data.get('puzzle')
        output_format = data.get('format', 'grid')
        
        parser = PuzzleParser()
        formatted = parser.to_string(puzzle, format=output_format)
        
        return jsonify({
            'formatted': formatted
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/examples', methods=['GET'])
def get_examples():
    """Get example puzzles."""
    examples = {
        'easy': {
            'name': 'Easy Puzzle',
            'puzzle': '530070000600195000098000060800060003400803001700020006060000280000419005000080079'
        },
        'medium': {
            'name': 'Medium Puzzle',
            'puzzle': '000060004700003006000090000000000000005180000000000000000050000900600001400020000'
        },
        'hard': {
            'name': 'Hard Puzzle',
            'puzzle': '000000000000003085001020000000005008000000000700100000000060702230500000000000000'
        }
    }
    
    return jsonify(examples)


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Server error'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)