from unittest.mock import patch

import pytest
from core.classes.game import Game
from tests.tests_app.utils.utils import get_all_text, safe_to_execute_game


@pytest.mark.visual_tests
def test_statistics_menu(
    game_app: Game, player_1_name: str, player_2_name: str
) -> None:
    """
    Проверка меню статистики:
    - Содержит всю ожидаемую информацию (имена игроков, победы, поражения).

    :param game_app: Экземпляр класса Game.
    :param player_1_name: Имя игрока №1.
    :param player_2_name: Имя игрока №2.
    :return: None.
    """

    # Сценарий: Выбираем количество игроков, игроки представляются, смотрим статистику, выходим из игры.
    user_inputs = ["2", player_1_name, player_2_name, "2", "3"]

    with patch("builtins.input", side_effect=user_inputs), patch(
        "builtins.print"
    ) as mock_print:
        safe_to_execute_game(game_app)
        printed_text = get_all_text(mock_print)

    assert f"1. {player_1_name}" in printed_text
    assert f"2. {player_2_name}" in printed_text
    assert printed_text.count("Побед: 0") == 2
    assert printed_text.count("Поражений: 0") == 2
