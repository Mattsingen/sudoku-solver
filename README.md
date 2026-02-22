# Sudoku Solver

This is a learning project for me to learn some Python.
The goal of this project is to create a modular Sudoku solver that can handle both regular and variant Sudoku puzzles. It can be run as a standalone Python program or as a local web application.

## Project Structure

```
sudoku-solver
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── solvers
│   │   ├── __init__.py
│   │   ├── base_solver.py
│   │   ├── regular_solver.py
│   │   └── variant_solver.py
│   ├── parsers
│   │   ├── __init__.py
│   │   └── puzzle_parser.py
│   ├── validators
│   │   ├── __init__.py
│   │   └── rule_validator.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── web
│   ├── __init__.py
│   ├── app.py
│   ├── templates
│   │   ├── index.html
│   │   └── solver.html
│   └── static
│       ├── style.css
│       └── script.js
├── tests
│   ├── __init__.py
│   ├── test_solvers.py
│   └── test_validators.py
├── requirements.txt
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd sudoku-solver
pip install -r requirements.txt
```

## Usage

### Standalone Application

To run the Sudoku solver as a standalone application, execute the following command:

```bash
python src/main.py
```

Follow the prompts to input your Sudoku puzzle.

### Web Application

To run the Sudoku solver as a web application, execute the following command:

```bash
python web/app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000` to access the Sudoku solver interface.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.