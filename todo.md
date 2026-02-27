# Project TODO

## In Progress / Next


## Backlog
- Update the basic functionality so that grids with a different size than 9x9 work, e.g. 4x4, 6x6, and 8x8x are not uncommon, but other sizes could appear.
    To make this some what usable in the first iterations should be limited to sizes between 4 and 9.  

- Update the cells so that the can hold the possible values.
    This could also give the possibility to have each cell added to different groups. Apart from supporting variant sudoku's it can be used to support the regular logical solver.

- Add a logical solver that tests for a multitude of logical steps, e.g. naked singles, hidden singles, pairs, triples, x-wings, etc.
    I think that to do this effectively each cell must be able to hold all the possible values and be removed by the steps.
    The https://www.sudokuwiki.org/ have a lot of information about the different strategies used in logical solvers.

- Update the web interface so that the users can do som manual solving with mouse and/or keyboard input.

- Add/expand PyTest coverage for helpers, parser, validator, solver.

- Add a simple CLI in src/main.py (parse input, validate, solve, print).

- Performance improvements (e.g., constraint propagation or heuristics).

- Variant Sudoku support (e.g., diagonal/X-sudoku).


## Completed
### 2026 Feb
- Finish Flask web interface end-to-end check (server start, UI load, solve/validate/format endpoints).

- Verify all demo/tests run from the new tests/ location and update any imports if needed.


## Notes
- Keep this file updated as tasks are completed or added.
