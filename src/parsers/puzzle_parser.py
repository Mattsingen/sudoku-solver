"""
Parser module for Sudoku puzzles.

This module provides parsing functionality to convert various input formats
into a standardized 9x9 2D list representation.
"""

import json
import re


class PuzzleParser:
    """
    Parses Sudoku puzzles from various input formats.
    
    Supported formats:
    - Single line string (81 characters)
    - Multi-line string (9 lines)
    - Grid format with separators
    - 2D list/array
    - JSON string or object
    
    Empty cells can be represented as: 0, '.', or '_'
    """
    
    def __init__(self):
        """Initialize the parser."""
        self.puzzle = None
        self.errors = []
    
    def parse(self, puzzle_input):
        """
        Main parsing method. Automatically detects format and parses.
        
        Args:
            puzzle_input: The puzzle in various formats (string, list, dict)
            
        Returns:
            list: 9x9 2D list representing the puzzle, or None if parsing fails
        """
        self.errors = []
        self.puzzle = None
        
        if puzzle_input is None:
            self.errors.append("No input provided")
            return None
        
        # Already a list - validate and clean
        if isinstance(puzzle_input, list):
            return self._parse_list(puzzle_input)
        
        # Dictionary or JSON object
        if isinstance(puzzle_input, dict):
            return self._parse_dict(puzzle_input)
        
        # String input - detect format
        if isinstance(puzzle_input, str):
            puzzle_input = puzzle_input.strip()
            
            # Try JSON first
            if puzzle_input.startswith('[') or puzzle_input.startswith('{'):
                try:
                    obj = json.loads(puzzle_input)
                    if isinstance(obj, list):
                        return self._parse_list(obj)
                    elif isinstance(obj, dict):
                        return self._parse_dict(obj)
                except json.JSONDecodeError:
                    pass
            
            # Single line format (81 characters)
            clean_input = re.sub(r'[^0-9._]', '', puzzle_input)
            if len(clean_input) == 81:
                return self._parse_single_line(clean_input)
            
            # Multi-line format
            lines = puzzle_input.split('\n')
            if len(lines) >= 9:
                return self._parse_multiline(lines)
            
            self.errors.append(f"Could not determine format of input string (length: {len(clean_input)})")
            return None
        
        self.errors.append(f"Unsupported input type: {type(puzzle_input)}")
        return None
    
    def _parse_single_line(self, line):
        """
        Parse a single line string of 81 characters.
        
        Args:
            line: String of 81 digits/dots/underscores
            
        Returns:
            list: 9x9 2D list or None
        """
        try:
            puzzle = []
            for i in range(9):
                row = []
                for j in range(9):
                    char = line[i * 9 + j]
                    value = self._char_to_int(char)
                    row.append(value)
                puzzle.append(row)
            
            self.puzzle = puzzle
            return puzzle
        except Exception as e:
            self.errors.append(f"Error parsing single line: {e}")
            return None
    
    def _parse_multiline(self, lines):
        """
        Parse multi-line string format.
        
        Args:
            lines: List of strings (at least 9 lines with puzzle data)
            
        Returns:
            list: 9x9 2D list or None
        """
        try:
            puzzle = []
            row_number = 0  # Track which row we're on (for error messages)
            
            for line in lines:
                # Skip empty lines or separator lines
                if not line.strip() or re.match(r'^[\s\-+|═║╔╗╚╝╠╣╦╩╬─│┌┐└┘├┤┬┴┼]+$', line):
                    continue
                
                # Extract digits and special characters for empty cells
                # Accept: 0-9, . (dot), _ (underscore), · (middle dot), * (asterisk), space
                chars = re.findall(r'[0-9._·*\s]', line)
                # Filter out pure spaces and keep only meaningful characters
                chars = [c for c in chars if c.strip() or c in '._·*0']
                
                # Check column count
                if len(chars) != 9:
                    self.errors.append(f"Row {len(puzzle) + 1}: expected 9 columns, found {len(chars)}")
                    return None
                
                if len(puzzle) < 9:
                    row = [self._char_to_int(c) for c in chars]
                    puzzle.append(row)
                else:
                    # We already have 9 rows, but found another valid row
                    self.errors.append(f"Too many rows: expected exactly 9 rows, found at least {len(puzzle) + 1}")
                    return None
            
            if len(puzzle) != 9:
                self.errors.append(f"Expected 9 rows, found {len(puzzle)}")
                return None
            
            self.puzzle = puzzle
            return puzzle
        except Exception as e:
            self.errors.append(f"Error parsing multi-line: {e}")
            return None
    
    def _parse_list(self, lst):
        """
        Parse and validate a 2D list.
        
        Args:
            lst: 2D list representing the puzzle
            
        Returns:
            list: Validated and cleaned 9x9 2D list or None
        """
        try:
            if not isinstance(lst, list) or len(lst) != 9:
                self.errors.append(f"List must have 9 rows, found {len(lst) if isinstance(lst, list) else 'not a list'}")
                return None
            
            puzzle = []
            for i, row in enumerate(lst):
                if not isinstance(row, list) or len(row) != 9:
                    self.errors.append(f"Row {i+1} must have 9 columns")
                    return None
                
                parsed_row = []
                for j, val in enumerate(row):
                    # Handle string values
                    if isinstance(val, str):
                        val = self._char_to_int(val)
                    
                    # Validate integer
                    if not isinstance(val, int) or val < 0 or val > 9:
                        self.errors.append(f"Invalid value at row {i+1}, col {j+1}: {val}")
                        return None
                    
                    parsed_row.append(val)
                
                puzzle.append(parsed_row)
            
            self.puzzle = puzzle
            return puzzle
        except Exception as e:
            self.errors.append(f"Error parsing list: {e}")
            return None
    
    def _parse_dict(self, dct):
        """
        Parse a dictionary format.
        
        Expected format: {"puzzle": [[...], ...]} or {"grid": [[...], ...]}
        
        Args:
            dct: Dictionary containing puzzle data
            
        Returns:
            list: 9x9 2D list or None
        """
        try:
            # Look for common keys
            puzzle_data = dct.get('puzzle') or dct.get('grid') or dct.get('board')
            
            if puzzle_data is None:
                self.errors.append("Dictionary must contain 'puzzle', 'grid', or 'board' key")
                return None
            
            return self._parse_list(puzzle_data)
        except Exception as e:
            self.errors.append(f"Error parsing dictionary: {e}")
            return None
    
    def _char_to_int(self, char):
        """
        Convert a character to integer value.
        
        Args:
            char: Character representing a cell ('0'-'9', '.', '_')
            
        Returns:
            int: Integer value 0-9
        """
        if char in '._·* ':
            return 0
        return int(char)
    
    def get_errors(self):
        """
        Get list of parsing errors.
        
        Returns:
            list: List of error message strings
        """
        return self.errors.copy()
    
    def to_string(self, puzzle=None, format='grid'):
        """
        Convert a puzzle to string representation.
        
        Args:
            puzzle: 9x9 2D list (uses last parsed puzzle if None)
            format: Output format ('simple', 'grid', 'line')
            
        Returns:
            str: String representation of the puzzle
        """
        if puzzle is None:
            puzzle = self.puzzle
        
        if puzzle is None:
            return ""
        
        if format == 'line':
            # Single line: 81 characters
            return ''.join(str(cell) if cell != 0 else '.' for row in puzzle for cell in row)
        
        elif format == 'simple':
            # Simple multi-line
            return '\n'.join(' '.join(str(cell) if cell != 0 else '.' for cell in row) for row in puzzle)
        
        elif format == 'grid':
            # Pretty grid with separators
            from src.utils.helpers import format_puzzle
            return format_puzzle(puzzle)
        
        return ""