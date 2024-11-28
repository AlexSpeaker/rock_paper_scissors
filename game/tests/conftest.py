from random import choices
from string import ascii_letters

import pytest
from core.classes.game import Game
from core.game import game


@pytest.fixture
def game_app() -> Game:
    return game


@pytest.fixture
def player_1_name() -> str:
    return "".join(choices(ascii_letters, k=20))


@pytest.fixture
def player_2_name() -> str:
    return "".join(choices(ascii_letters, k=20))
