# Tic Tac Toe Game

## Overview

This is an advanced implementation of the classic Tic Tac Toe game with a modern graphical user interface built using Python's Tkinter library. The game features multiple difficulty levels when playing against the computer, visual animations, and a sleek gradient background.

## Features

- **Beautiful UI**: Gradient background, animated moves, and a clean interface.
- **Multiple Game Modes**:
  - Play against a friend (2-player mode).
  - Play against the computer with three difficulty levels.
- **Computer AI Difficulty Levels**:
  - **Easy**: Computer makes random moves.
  - **Medium**: Computer can block your winning moves and make its own winning moves.
  - **Hard**: Computer uses the minimax algorithm for optimal play.
- **Score Tracking**: Keeps track of wins for both players.
- **Visual Feedback**: Winning lines are highlighted in green.
- **Game Controls**: Restart current game or return to the main menu.

## How to Play

1. Launch the game by running:
   ```sh
   python tictactoe_v4.py
   ```
2. From the main menu, select your preferred game mode:
   - **"Play with Friend"** for a 2-player game.
   - **"Play with Computer"** and select a difficulty level.
3. Enter player name(s) when prompted.
4. Take turns placing X's and O's on the board by clicking on the grid.
5. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
6. If all squares are filled and no player has three in a row, the game is a tie.

## Technical Details

The game implements several algorithms for the computer AI:

- **Easy**: Simple random selection of available spaces.
- **Medium**: Prioritizes winning moves and blocking opponent's winning moves.
- **Hard**: Uses the minimax algorithm with alpha-beta pruning to make optimal decisions.

The UI features smooth animations and visual cues to enhance the gaming experience.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Running the Game

```sh
python tictactoe_v4.py
```

## Controls

- Click on any empty cell to place your mark (X or O).
- Use the **"Restart"** button to reset the current game.
- Use the **"Menu"** button to return to the main menu.

## Credits

This game was developed as an educational project to demonstrate GUI programming with Tkinter and AI algorithms for game strategy.
Created by **@flowstxte**
