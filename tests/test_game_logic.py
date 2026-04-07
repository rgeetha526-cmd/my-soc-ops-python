from app.data import FREE_SPACE, QUESTIONS
from app.game_logic import (
    CENTER_INDEX,
    check_bingo,
    generate_board,
    get_winning_square_ids,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData, GameMode


class TestGenerateBoard:
    def test_board_has_25_squares(self) -> None:
        board = generate_board()
        assert len(board) == 25

    def test_center_is_free_space(self) -> None:
        board = generate_board()
        center = board[CENTER_INDEX]
        assert center.is_free_space is True
        assert center.is_marked is True
        assert center.text == FREE_SPACE

    def test_non_center_squares_are_not_free_space(self) -> None:
        board = generate_board()
        for i, square in enumerate(board):
            if i != CENTER_INDEX:
                assert square.is_free_space is False
                assert square.is_marked is False

    def test_all_questions_from_pool(self) -> None:
        board = generate_board()
        texts = {s.text for s in board if not s.is_free_space}
        assert texts.issubset(set(QUESTIONS))

    def test_squares_have_sequential_ids(self) -> None:
        board = generate_board()
        for i, square in enumerate(board):
            assert square.id == i

    def test_board_is_shuffled(self) -> None:
        """Verify two boards aren't identical (high probability)."""
        board1 = generate_board()
        board2 = generate_board()
        texts1 = [s.text for s in board1]
        texts2 = [s.text for s in board2]
        assert texts1 != texts2


class TestToggleSquare:
    def test_toggle_marks_unmarked_square(self) -> None:
        board = generate_board()
        square_id = 0
        assert board[square_id].is_marked is False
        new_board = toggle_square(board, square_id)
        assert new_board[square_id].is_marked is True

    def test_toggle_unmarks_marked_square(self) -> None:
        board = generate_board()
        board = toggle_square(board, 0)
        assert board[0].is_marked is True
        board = toggle_square(board, 0)
        assert board[0].is_marked is False

    def test_toggle_does_not_affect_free_space(self) -> None:
        board = generate_board()
        new_board = toggle_square(board, CENTER_INDEX)
        assert new_board[CENTER_INDEX].is_marked is True

    def test_toggle_returns_new_list(self) -> None:
        board = generate_board()
        new_board = toggle_square(board, 0)
        assert board is not new_board


class TestCheckBingo:
    def _make_board(self, marked_ids: set[int]) -> list[BingoSquareData]:
        board = generate_board()
        result: list[BingoSquareData] = []
        for square in board:
            if square.id in marked_ids or square.is_free_space:
                result.append(
                    BingoSquareData(
                        id=square.id,
                        text=square.text,
                        is_marked=True,
                        is_free_space=square.is_free_space,
                    )
                )
            else:
                result.append(square)
        return result

    def test_no_bingo_initially(self) -> None:
        board = generate_board()
        assert check_bingo(board) is None

    def test_row_bingo(self) -> None:
        board = self._make_board({0, 1, 2, 3, 4})
        result = check_bingo(board)
        assert result is not None
        assert result.type == "row"
        assert result.squares == [0, 1, 2, 3, 4]

    def test_column_bingo(self) -> None:
        board = self._make_board({0, 5, 10, 15, 20})
        result = check_bingo(board)
        assert result is not None
        assert result.type == "column"
        assert result.squares == [0, 5, 10, 15, 20]

    def test_diagonal_bingo(self) -> None:
        board = self._make_board({0, 6, 18, 24})
        result = check_bingo(board)
        assert result is not None
        assert result.type == "diagonal"
        assert result.squares == [0, 6, 12, 18, 24]

    def test_partial_line_no_bingo(self) -> None:
        board = self._make_board({0, 1, 2, 3})
        assert check_bingo(board) is None

    def test_scavenger_hunt_win_all_marked(self) -> None:
        board = self._make_board(set(range(25)))  # all marked
        result = check_bingo(board, mode=GameMode.SCAVENGER_HUNT)
        assert result is not None
        assert result.type == "all"
        assert result.squares == list(range(25))

    def test_scavenger_hunt_partial_no_win(self) -> None:
        board = self._make_board({0, 1, 2, 3, 4})
        result = check_bingo(board, mode=GameMode.SCAVENGER_HUNT)
        assert result is None

    def test_card_deck_shuffle_win_center_marked(self) -> None:
        board = generate_board(GameMode.CARD_DECK_SHUFFLE)
        # Mark the center square
        board = toggle_square(board, 12)
        result = check_bingo(board, mode=GameMode.CARD_DECK_SHUFFLE)
        assert result is not None
        assert result.type == "center"
        assert result.squares == [12]

    def test_card_deck_shuffle_center_not_marked_no_win(self) -> None:
        board = generate_board(GameMode.CARD_DECK_SHUFFLE)
        # Mark some other squares but not center
        board = toggle_square(board, 0)
        board = toggle_square(board, 1)
        board = toggle_square(board, 2)
        result = check_bingo(board, mode=GameMode.CARD_DECK_SHUFFLE)
        assert result is None


class TestGetWinningSquareIds:
    def test_none_line_returns_empty_set(self) -> None:
        assert get_winning_square_ids(None) == set()

    def test_returns_square_ids(self) -> None:
        line = BingoLine(type="row", index=0, squares=[0, 1, 2, 3, 4])
        assert get_winning_square_ids(line) == {0, 1, 2, 3, 4}


class TestGameMode:
    def test_game_mode_enum_values(self) -> None:
        assert GameMode.BINGO == "bingo"
        assert GameMode.SCAVENGER_HUNT == "scavenger_hunt"
        assert GameMode.CARD_DECK_SHUFFLE == "card_deck_shuffle"
