from random import choices
from string import ascii_letters

import pytest
from classes.game.game import Game
from classes.player.player import Player


@pytest.fixture
def human_player() -> Player:
    return Player(player_name="hp1".join(choices(ascii_letters, k=10)))


@pytest.fixture
def another_human_player() -> Player:
    return Player(player_name="hp2".join(choices(ascii_letters, k=10)))


@pytest.fixture
def computer_player() -> Player:
    return Player(player_name="cp".join(choices(ascii_letters, k=10)), computer=True)


@pytest.fixture
def game_one_player(human_player: Player, computer_player: Player) -> Game:
    return Game(human_player, computer_player)


@pytest.fixture
def game_two_player(human_player: Player, another_human_player: Player) -> Game:
    return Game(human_player, another_human_player)
