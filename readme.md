# Tic Tac Toe Game

## Overview
An advanced implementation of the classic Tic Tac Toe game with a modern graphical user interface built using Python's Tkinter.  
The game includes multiple difficulty levels, smooth animations, score tracking, and a gradient-themed design.

<p align="center">
  <img src="https://raw.githubusercontent.com/flowstxte/Project-TicTacToe/refs/heads/main/ss1.png" width="45%" />
  <img src="https://raw.githubusercontent.com/flowstxte/Project-TicTacToe/refs/heads/main/ss2.png" width="45%" />
</p>

---

## Features
- **Modern UI**: Gradient background, clean interface, and animated moves.  
- **Game Modes**:  
  - Two-player (friend vs friend)  
  - Single-player against computer (3 difficulty levels)  
- **Computer AI**:  
  - Easy → Random moves  
  - Medium → Blocks opponent and makes winning moves  
  - Hard → Minimax algorithm with alpha-beta pruning  
- **Score Tracking**: Keeps record of player wins.  
- **Visual Feedback**: Highlights winning lines in green.  
- **Game Controls**: Restart or return to main menu.  

---

## How to Play
1. Run the game.
2. Choose a mode:

   * **Play with Friend** → 2-player game
   * **Play with Computer** → select difficulty
3. Enter player name(s).
4. Take turns placing X or O by clicking on the grid.
5. First to align three marks (row, column, or diagonal) wins.
6. If the board is full with no winner, the match ends in a tie.

---

## Technical Details

* **Easy Mode**: Random move selection.
* **Medium Mode**: Detects and blocks opponent’s win, or makes its own.
* **Hard Mode**: Implements the minimax algorithm with alpha-beta pruning.

---

## Requirements
<p>
  <img src="https://skillicons.dev/icons?i=python" />  
</p>

* Python 3.x
* Tkinter (comes pre-installed with most Python distributions)

---

## Running the Game

```sh
python tictactoe_v4.py
```

---

## Credits

Developed as an educational project to demonstrate GUI programming with Tkinter and AI game strategy.
Created by **[@flowstxte](https://github.com/flowstxte)**
