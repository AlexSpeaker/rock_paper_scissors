import re
from unittest.mock import patch

import pytest
from classes.game.game import Game
from classes.player.player import Player
from tests.tests_app.utils.utils import get_all_text, safe_to_execute_game


@pytest.mark.parametrize(
    "human_player_choice, another_human_player_choice, expected_result",
    [
        ("камень", "ножницы", "выиграл"),
        ("камень", "камень", "ничья"),
        ("камень", "бумага", "проиграл"),
    ],
)
def test_rules_game(
    game_two_player: Game,
    human_player: Player,
    another_human_player: Player,
    human_player_choice: str,
    another_human_player_choice: str,
    expected_result: str,
) -> None:
    """
    Проверяем категорию 'Статистика'.
    - При победе добавляется победа. А у противника добавляется поражение.
    - При поражении добавляется поражение. А у противника добавляется победа.
    - Если ничья - ничего не добавляется.

    :param game_two_player: Экземпляр класса Game.
    :param human_player: 1-й игрок (Экземпляр класса Player).
    :param another_human_player: 2-й игрок (Экземпляр класса Player).
    :param human_player_choice: Выбранный элемент 1-го игрока (str).
    :param another_human_player_choice: Выбранный элемент 2-го игрока (str).
    :param expected_result: Как должна закончится игра для 1-го игрока.
    :return: None
    """

    choice_data = {"камень": "1", "ножницы": "2", "бумага": "3"}
    # Сценарий: Пользователь начинает игру. Пользователи по очереди выбирают элемент. После заходим в раздел 'Статистика'.
    user_inputs = [
        "1",
        choice_data[human_player_choice],
        choice_data[another_human_player_choice],
        "2",
    ]
    with (
        patch("builtins.input", side_effect=user_inputs),
        patch("builtins.print") as mock_print,
    ):

        safe_to_execute_game(game_two_player)
        printed_text = get_all_text(mock_print)

    match expected_result:
        case "ничья":
            assert re.search(
                rf"{human_player.name}.+Побед: 0.+Поражений: 0[^*]+", printed_text
            )
            assert re.search(
                rf"{another_human_player.name}.+Побед: 0.+Поражений: 0[^*]+",
                printed_text,
            )
        case "выиграл":
            assert re.search(
                rf"{human_player.name}.+Побед: 1.+Поражений: 0[^*]+", printed_text
            )
            assert re.search(
                rf"{another_human_player.name}.+Побед: 0.+Поражений: 1[^*]+",
                printed_text,
            )
        case "проиграл":
            assert re.search(
                rf"{human_player.name}.+Побед: 0.+Поражений: 1[^*]+", printed_text
            )
            assert re.search(
                rf"{another_human_player.name}.+Побед: 1.+Поражений: 0[^*]+",
                printed_text,
            )
