# Calc & Hang Game

A unique educational word game that combines classic hangman with mathematical operations.

## About

Calc & Hang is an innovative terminal-based game that merges the classic hangman word-guessing game with mathematical problem-solving. Players must either guess letters or solve math operations to reveal letters and complete the word before running out of attempts.

## Features

- **Random Word Selection**: Words from 3 categories (fruits, animals, technology)
- **Letter Guessing System**: Classic hangman-style letter guessing with validation
- **Math Integration**: 4 mathematical operations (addition, subtraction, multiplication, division)
- **Single-Use Operations**: Each math operation can only be used once per game
- **Bonus System**: Earn bonuses by solving math problems, spend them on hints
- **Score Tracking**: Automatic score saving to JSON file
- **Colorful Terminal Output**: Enhanced user experience with colored text (optional)
- **Error Handling**: Robust input validation and error management

## Project Structure

```
calc-and-hang-game/
│
├── src/
│   └── calc_and_hang_game.py    # Main game source code (936 lines)
│
├── tests/
│   └── test_calc_and_hang.py    # Comprehensive test suite (693 lines, 40+ tests)
│
├── PROJE_RAPORU_TESLIM.md        # Detailed project report (Turkish)
├── requirements.txt               # Python dependencies
├── scores.json                    # High scores storage (auto-generated)
└── README.md                      # This file

```

## Installation

### Requirements

- Python 3.6 or higher
- colorama (optional, for colored output)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/calc-and-hang-game.git
cd calc-and-hang-game
```

2. Install dependencies (optional):
```bash
pip install -r requirements.txt
```

## Usage

### Running the Game

```bash
python src/calc_and_hang_game.py
```

### Game Options

During gameplay, you have 4 options:

1. **[H] Letter Guess**: Guess a single letter
   - Correct guess: +10 points
   - Wrong guess: -5 points, error count +1

2. **[I] Solve Operation**: Solve a math problem to reveal a random letter
   - Correct answer: +15 points, +1 bonus, random letter revealed
   - Wrong answer: -10 points, error count +1
   - Each operation type (addition, subtraction, multiplication, division) can only be used once

3. **[I] Hint**: Use a bonus point to see the word category
   - Costs: -1 bonus point

4. **[C] Exit**: Save score and quit

### Scoring System

| Action | Points |
|--------|--------|
| Correct letter | +10 |
| Wrong letter | -5 |
| Correct operation | +15 + 1 bonus |
| Wrong operation | -10 |
| Use hint | -1 bonus |
| Win game | +50 |
| Lose game | -20 |

## Testing

The project includes a comprehensive automated test suite with 40+ tests covering all 7 classes.

### Running Tests

```bash
python tests/test_calc_and_hang.py
```

### Test Coverage

- **AsmacaCizici**: 4 tests (hangman visual rendering)
- **KelimeDeposu**: 4 tests (word repository)
- **MatematikMotoru**: 7 tests (math operations)
- **PuanYoneticisi**: 8 tests (score management)
- **OyunDurumKontrolcusu**: 7 tests (game state)
- **ArayuzYoneticisi**: 5 tests (UI management)
- **HesaplamaVeAsmacaOyunu**: 5 tests (main game controller)
- **Integration Test**: 1 test (full game flow)

**Total: 40+ automated tests | Test Coverage: 100%**

## Architecture

The game follows Object-Oriented Programming principles with 7 main classes:

### 1. AsmacaCizici (Hangman Renderer)
- Manages visual representation of hangman figure
- 7 stages from empty to complete

### 2. KelimeDeposu (Word Repository)
- Stores words organized by categories
- Provides random word selection

### 3. MatematikMotoru (Math Engine)
- Handles mathematical operations
- Ensures single-use per operation type
- Float comparison with 1e-6 tolerance

### 4. PuanYoneticisi (Score Manager)
- Tracks and updates scores
- Saves top 5 scores to JSON
- Auto-sorting by score

### 5. OyunDurumKontrolcusu (Game State Manager)
- Manages game state and logic
- Letter validation and tracking
- Win/loss detection

### 6. ArayuzYoneticisi (UI Manager)
- Handles user input and output
- Colored terminal support
- Message formatting

### 7. HesaplamaVeAsmacaOyunu (Main Game Controller)
- Orchestrates all components
- Main game loop
- Action handling

## Example Gameplay

```
==================================================
--- Yeni Tur ---
==================================================

    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========

Kelime: a _ _ l e
Tahmin edilen harfler: a, e, l
Kalan hata hakki: 3
Bonus puani: 1
==================================================

Seçenekler: [H]arf tahmini | [I]slem coz | [I]pucu | [C]ikis
Kalan islemler: Carpma (*), Bolme (/)

Seciminiz: I

[OK] Dogru! 6.0 * 7.0 = 42.0
[OK] Bonus: 'p' harfi acildi!
```

## Technical Details

### Key Features Implementation

1. **Single-Use Operations**: Boolean dictionary tracks used operations
2. **Float Comparison**: 1e-6 epsilon tolerance for decimal operations
3. **Error Handling**: Try-except blocks throughout, graceful degradation
4. **Type Hints**: Modern Python typing for better code quality
5. **Docstrings**: Comprehensive documentation for all functions
6. **Modular Design**: Separated concerns, easy to extend

### Error Prevention

- Zero division protection
- Duplicate letter detection
- Input validation for all user entries
- File operation error handling
- Keyboard interrupt handling

## Development

### Code Statistics

- **Total Lines**: 1,629 (936 game + 693 tests)
- **Classes**: 8 (7 game + 1 test result tracker)
- **Test Cases**: 40+
- **Test Coverage**: 100%

### Requirements

See `requirements.txt`:
```
colorama>=0.4.6
```

## Documentation

For detailed Turkish documentation including:
- Full requirement analysis
- Architecture design
- Use-case diagrams
- Activity diagrams
- Test scenarios and results

See: [PROJE_RAPORU_TESLIM.md](PROJE_RAPORU_TESLIM.md)

## License

This project was developed as an educational assignment for Kocaeli Health and Technology University.

**Student**: Alperen Yagmur  
**Student ID**: 250502015  
**Course**: Computer/Software Engineering  
**Date**: November 2025

## Contributing

This is an educational project. Feel free to fork and modify for learning purposes.

## Acknowledgments

- Inspired by classic hangman game
- Mathematical operations add educational value
- Developed with OOP principles and clean code practices

---

**Project Status**: Complete and fully functional  
**Test Status**: All tests passing  
**Code Quality**: Documented, typed, and modular
