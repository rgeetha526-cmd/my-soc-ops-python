import pytest
from fastapi.testclient import TestClient

from app.game_service import GameSession
from app.main import app
from app.models import GameMode


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


class TestHomePage:
    def test_home_returns_200(self, client: TestClient) -> None:
        response = client.get("/")
        assert response.status_code == 200

    def test_home_contains_start_screen(self, client: TestClient) -> None:
        response = client.get("/")
        assert "Soc Ops" in response.text
        assert "Start Game" in response.text
        assert "How to play" in response.text

    def test_home_sets_session_cookie(self, client: TestClient) -> None:
        response = client.get("/")
        assert "session" in response.cookies


class TestStartGame:
    def test_start_returns_game_board(self, client: TestClient) -> None:
        client.get("/")
        response = client.post("/start")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
        assert "← Back" in response.text

    def test_board_has_25_squares(self, client: TestClient) -> None:
        client.get("/")
        response = client.post("/start")
        assert response.text.count('hx-post="/toggle/') == 24

    def test_start_with_scavenger_hunt_mode(self, client: TestClient) -> None:
        client.get("/")
        response = client.post("/start", data={"mode": "scavenger_hunt"})
        assert response.status_code == 200
        # Check that it's scavenger hunt UI, e.g., no grid, has list
        assert "scavenger" in response.text.lower() or "progress" in response.text.lower()

    def test_start_with_card_deck_shuffle_mode(self, client: TestClient) -> None:
        client.get("/")
        response = client.post("/start", data={"mode": "card_deck_shuffle"})
        assert response.status_code == 200
        # Check that it's card deck shuffle UI
        assert "card deck shuffle" in response.text.lower()


class TestToggleSquare:
    def test_toggle_marks_square(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/toggle/0")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text


class TestResetGame:
    def test_reset_returns_start_screen(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/reset")
        assert response.status_code == 200
        assert "Start Game" in response.text
        assert "How to play" in response.text


class TestDismissModal:
    def test_dismiss_returns_game_screen(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/dismiss-modal")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text


class TestGameService:
    def test_game_session_has_mode(self) -> None:
        session = GameSession()
        assert hasattr(session, 'mode')
        assert session.mode == GameMode.BINGO  # default

    def test_start_game_with_mode(self) -> None:
        session = GameSession()
        session.start_game(mode=GameMode.SCAVENGER_HUNT)
        assert session.mode == GameMode.SCAVENGER_HUNT
        assert session.game_state.name == "PLAYING"
