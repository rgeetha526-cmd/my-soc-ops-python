import functools
import random

from app.data import FREE_SPACE, QUESTIONS
from app.models import BingoLine, BingoSquareData, GameMode

BOARD_SIZE: int = 5
CENTER_INDEX: int = 12  # 5x5 grid, center is index 12 (row 2, col 2)


def generate_board(mode: GameMode = GameMode.BINGO) -> list[BingoSquareData]:
    """Generate a new 5x5 bingo board."""
    if mode == GameMode.CARD_DECK_SHUFFLE:
        # For card deck shuffle, create a single card in the center
        question = random.choice(QUESTIONS)
        board = [
            BingoSquareData(id=i, text="", is_marked=False, is_free_space=False)
            for i in range(BOARD_SIZE * BOARD_SIZE)
        ]
        # Set the center square
        board[CENTER_INDEX] = BingoSquareData(
            id=CENTER_INDEX, text=question, is_marked=False, is_free_space=False
        )
        return board
    else:
        questions: list[str] = list(random.sample(QUESTIONS, 24))
        question_iter = iter(questions)
        return [
            BingoSquareData(id=i, text=FREE_SPACE, is_marked=True, is_free_space=True)
            if i == CENTER_INDEX
            else BingoSquareData(id=i, text=next(question_iter))
            for i in range(BOARD_SIZE * BOARD_SIZE)
        ]


def toggle_square(
    board: list[BingoSquareData], square_id: int
) -> list[BingoSquareData]:
    """Toggle a square's marked state. Returns a new board list."""
    return [
        sq.model_copy(update={"is_marked": not sq.is_marked})
        if sq.id == square_id and not sq.is_free_space
        else sq
        for sq in board
    ]


@functools.cache
def _get_winning_lines() -> tuple[BingoLine, ...]:
    """Get all possible winning lines (cached)."""
    lines: list[BingoLine] = []

    for row in range(BOARD_SIZE):
        squares: list[int] = [row * BOARD_SIZE + col for col in range(BOARD_SIZE)]
        lines.append(BingoLine(type="row", index=row, squares=squares))

    for col in range(BOARD_SIZE):
        squares = [row * BOARD_SIZE + col for row in range(BOARD_SIZE)]
        lines.append(BingoLine(type="column", index=col, squares=squares))

    lines.append(BingoLine(type="diagonal", index=0, squares=[0, 6, 12, 18, 24]))
    lines.append(BingoLine(type="diagonal", index=1, squares=[4, 8, 12, 16, 20]))

    return tuple(lines)


def check_bingo(board: list[BingoSquareData], mode: GameMode = GameMode.BINGO) -> BingoLine | None:
    """Check if there's a bingo and return the winning line."""
    if mode == GameMode.SCAVENGER_HUNT:
        return _check_scavenger_bingo(board)
    if mode == GameMode.CARD_DECK_SHUFFLE:
        # For card deck shuffle, win when the center square is marked
        if board[CENTER_INDEX].is_marked:
            return BingoLine(type="center", index=0, squares=[CENTER_INDEX])
        return None
    if len(board) < BOARD_SIZE * BOARD_SIZE:
        return None
    return next(
        (
            line
            for line in _get_winning_lines()
            if all(board[idx].is_marked for idx in line.squares)
        ),
        None,
    )


def _check_scavenger_bingo(board: list[BingoSquareData]) -> BingoLine | None:
    """Check for scavenger hunt win: all squares marked."""
    if all(sq.is_marked for sq in board):
        return BingoLine(type="all", index=0, squares=list(range(len(board))))
    return None


def get_winning_square_ids(line: BingoLine | None) -> set[int]:
    """Get the square IDs that are part of a winning line."""
    return set(line.squares) if line else set()
