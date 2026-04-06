---
description: Bingo game mechanics and logic for the Soc Ops application
---

# Bingo Game Logic

## Overview
The Soc Ops application implements a 5x5 bingo game where players mark squares based on finding other players who match the questions. The center square is always marked as a free space.

## Core Mechanics

### Board Generation
- 5x5 grid (25 squares total)
- Center square (index 12) is always marked and contains "FREE SPACE"
- Remaining 24 squares filled with random questions from the QUESTIONS list
- Questions are shuffled to ensure variety

### Square Interaction
- Players can toggle squares between marked/unmarked states
- Free space square cannot be toggled (always marked)
- Marking represents finding another player who matches the question

### Winning Conditions
- **Rows**: Any complete horizontal line (5 marked squares)
- **Columns**: Any complete vertical line (5 marked squares)  
- **Diagonals**: Two possible diagonals (top-left to bottom-right, top-right to bottom-left)
- Game ends when any winning line is achieved

### Winning Line Detection
- Check all possible lines after each move
- Return the first winning line found (if any)
- Highlight winning squares for verification

## Implementation Notes
- Use immutable data structures (new board returned on changes)
- Cache winning lines calculation for performance
- Board state managed through BingoSquareData models
- Session-based game state persistence

## Question Guidelines
- Questions should be inclusive and safe
- Mix of easy, medium, and challenging prompts
- Focus on conversation starters and fun interactions
- Avoid sensitive topics (health, finances, politics, relationships)
