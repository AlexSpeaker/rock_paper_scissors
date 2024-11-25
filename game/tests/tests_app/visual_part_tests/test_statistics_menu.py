from unittest.mock import patch

import pytest
from classes.game.game import Game
from classes.player.player import Player
from tests.tests_app.utils.utils import get_all_text, safe_to_execute_game


@pytest.mark.visual_tests
def test_statistics_menu(
    game_one_player: Game, computer_player: Player, human_player: Player
) -> None:
    """
    Проверка меню статистики:
    - Содержит всю ожидаемую информацию (имена игроков, победы, поражения).

    :param game_one_player: Экземпляр класса Game.
    :return: None
    """

    # Сценарий: Пользователь заходит в статистику. Выходит из игры.
    user_inputs = ["2", "3"]

    with patch("builtins.input", side_effect=user_inputs), patch(
        "builtins.print"
    ) as mock_print:
        safe_to_execute_game(game_one_player)
        printed_text = get_all_text(mock_print)

    assert computer_player.name in printed_text
    assert human_player.name in printed_text
    assert printed_text.count("Побед: 0") == 2
    assert printed_text.count("Поражений: 0") == 2
