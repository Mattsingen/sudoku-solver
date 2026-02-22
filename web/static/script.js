// ============================================
// DOM Elements
// ============================================

const puzzleInput = document.getElementById('puzzle-input');
const validateBtn = document.getElementById('validate-btn');
const solveBtn = document.getElementById('solve-btn');
const clearBtn = document.getElementById('clear-btn');
const statusMessage = document.getElementById('status-message');
const outputSection = document.getElementById('output-section');
const puzzleGrid = document.getElementById('puzzle-grid');
const solutionGrid = document.getElementById('solution-grid');
const statTime = document.getElementById('stat-time');
const statSteps = document.getElementById('stat-steps');
const copyBtn = document.getElementById('copy-solution-btn');
const newPuzzleBtn = document.getElementById('new-puzzle-btn');

let currentPuzzle = null;
let currentSolution = null;

// ============================================
// Event Listeners
// ============================================

document.addEventListener('DOMContentLoaded', function () {
    setupEventListeners();
    loadExamples();
});

function setupEventListeners() {
    validateBtn.addEventListener('click', validatePuzzle);
    solveBtn.addEventListener('click', solvePuzzle);
    clearBtn.addEventListener('click', clearInput);
    copyBtn.addEventListener('click', copySolution);
    newPuzzleBtn.addEventListener('click', newPuzzle);

    // Example buttons
    document.querySelectorAll('.example-btn').forEach(btn => {
        btn.addEventListener('click', loadExample);
    });

    // Allow Enter key to solve
    puzzleInput.addEventListener('keydown', function (e) {
        if (e.ctrlKey && e.key === 'Enter') {
            solvePuzzle();
        }
    });
}

// ============================================
// Main Functions
// ============================================

async function validatePuzzle() {
    const input = puzzleInput.value.trim();
    if (!input) {
        showMessage('Please enter a puzzle first', 'error');
        return;
    }

    try {
        showMessage('Validating puzzle...', 'info');
        const response = await fetch('/api/validate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ puzzle: input })
        });

        const data = await response.json();

        if (data.valid) {
            const status = data.complete ? 'complete' : 'valid (incomplete)';
            showMessage(`✓ Puzzle is ${status}!`, 'success');
        } else {
            showMessage('✗ Invalid puzzle:\n' + data.errors.join('\n'), 'error');
        }
    } catch (error) {
        showMessage('Error validating puzzle: ' + error.message, 'error');
    }
}

async function solvePuzzle() {
    const input = puzzleInput.value.trim();
    if (!input) {
        showMessage('Please enter a puzzle first', 'error');
        return;
    }

    try {
        solveBtn.disabled = true;
        showMessage('Solving puzzle...', 'info');

        const response = await fetch('/api/solve', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ puzzle: input })
        });

        const data = await response.json();

        if (data.success) {
            currentPuzzle = extractPuzzleFromInput(input);
            currentSolution = data.solution;

            // Parse input to get original puzzle
            const parser = new PuzzleParser();
            currentPuzzle = parser.parse(input);

            displayResults(data);
            showMessage('✓ Puzzle solved successfully!', 'success');
        } else {
            showMessage('✗ Error: ' + (data.errors ? data.errors.join('\n') : 'Unknown error'), 'error');
        }
    } catch (error) {
        showMessage('Error solving puzzle: ' + error.message, 'error');
    } finally {
        solveBtn.disabled = false;
    }
}

function displayResults(data) {
    outputSection.style.display = 'block';

    // Display grids
    renderGrid(puzzleGrid, currentPuzzle, 'given');
    renderGrid(solutionGrid, data.solution, 'filled');

    // Update stats
    statTime.textContent = data.time_ms + ' ms';
    statSteps.textContent = data.steps.toLocaleString();

    // Scroll to results
    setTimeout(() => {
        outputSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
}

function renderGrid(gridElement, puzzle, cellClass) {
    gridElement.innerHTML = '';

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const cell = document.createElement('div');
            cell.className = 'sudoku-cell ' + cellClass;
            const value = puzzle[i][j];
            cell.textContent = value === 0 ? '' : value;

            if (value === 0) {
                cell.classList.add('empty');
            } else if (cellClass === 'given') {
                // In the given puzzle, non-zero values were given
                if (currentSolution && currentSolution[i][j] !== value) {
                    cell.classList.remove('given');
                }
            }

            gridElement.appendChild(cell);
        }
    }
}

async function loadExample(e) {
    const exampleType = e.target.dataset.example;

    try {
        const response = await fetch('/api/examples');
        const examples = await response.json();

        if (examples[exampleType]) {
            puzzleInput.value = examples[exampleType].puzzle;
            showMessage(`Loaded: ${examples[exampleType].name}`, 'info');
        }
    } catch (error) {
        showMessage('Error loading example: ' + error.message, 'error');
    }
}

function clearInput() {
    puzzleInput.value = '';
    outputSection.style.display = 'none';
    hideMessage();
    puzzleInput.focus();
}

function newPuzzle() {
    clearInput();
}

async function copySolution() {
    if (!currentSolution) {
        showMessage('No solution to copy', 'error');
        return;
    }

    try {
        const response = await fetch('/api/format', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                puzzle: currentSolution,
                format: 'line'
            })
        });

        const data = await response.json();
        const text = data.formatted;

        await navigator.clipboard.writeText(text);
        showMessage('✓ Solution copied to clipboard!', 'success');
    } catch (error) {
        showMessage('Error copying: ' + error.message, 'error');
    }
}

// ============================================
// Helper Functions
// ============================================

function showMessage(text, type = 'info') {
    statusMessage.innerHTML = text;
    statusMessage.className = 'status-message show ' + type;
}

function hideMessage() {
    statusMessage.className = 'status-message';
    statusMessage.innerHTML = '';
}

function loadExamples() {
    // Examples are loaded on demand
}

function extractPuzzleFromInput(input) {
    // Try to parse as 2D array from string representation
    try {
        if (input.startsWith('[')) {
            return JSON.parse(input);
        }
    } catch (e) {
        // Not JSON, continue
    }
    return null;
}

// Simple puzzle parser (client-side version)
class PuzzleParser {
    parse(input) {
        input = input.trim();

        // Try JSON first
        if (input.startsWith('[') || input.startsWith('{')) {
            try {
                const obj = JSON.parse(input);
                if (Array.isArray(obj)) return obj;
                if (obj.puzzle) return obj.puzzle;
            } catch (e) {
                // Not JSON
            }
        }

        // Try single line (81 characters)
        const cleanInput = input.replace(/[^0-9._]/g, '');
        if (cleanInput.length === 81) {
            const puzzle = [];
            for (let i = 0; i < 9; i++) {
                const row = [];
                for (let j = 0; j < 9; j++) {
                    const char = cleanInput[i * 9 + j];
                    row.push(char === '.' || char === '_' ? 0 : parseInt(char));
                }
                puzzle.push(row);
            }
            return puzzle;
        }

        // Try multi-line
        const lines = input.split('\n');
        if (lines.length >= 9) {
            const puzzle = [];
            for (const line of lines) {
                const chars = line.match(/[0-9._]/g) || [];
                if (chars.length === 9) {
                    puzzle.push(chars.map(c => c === '.' || c === '_' ? 0 : parseInt(c)));
                }
                if (puzzle.length === 9) break;
            }
            if (puzzle.length === 9) return puzzle;
        }

        return null;
    }
}