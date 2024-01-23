# Battleship Game

## Overview

Welcome to the Battleship game! This simple text-based game allows you to play the classic Battleship game in the terminal. Sink the computer's ships by making strategic guesses, and enjoy the thrill of naval warfare!

## Purpose

The purpose of this Python application is to provide a fun and interactive gaming experience. The Battleship game allows users to engage in a strategic naval battle with the computer, testing their skills in guessing ship locations and sinking the opponent's fleet.

## Value to Users

- **Entertainment:** Enjoy a classic board game in a digital format.
- **Strategic Thinking:** Sharpen your strategic thinking skills by making calculated guesses to sink computer ships.
- **Terminal-Based Experience:** Play the game directly in the terminal, offering a simple and accessible interface.

## How to Play

1. **Game Setup:**
   - The game begins by randomly placing a specified number of ships on an 8x8 grid.
   - Your goal is to guess the coordinates of the computer's ships and sink them all.

2. **Making a Guess:**
   - The game prompts you to enter the row and column coordinates for your guess.
   - Row and column indices are zero-based, starting from 0.
   - Input is validated to ensure it falls within the valid range.

3. **Game Feedback:**
   - After each guess, the game provides feedback:
     - If you hit a ship, it congratulates you and marks the hit on the board.
     - If you miss, it informs you that you've missed.
     - If you've already guessed a position, it prompts you to try again.

4. **Winning the Game:**
   - The game continues until you sink all the computer's ships.
   - A victory message is displayed once all ships are successfully sunk.


