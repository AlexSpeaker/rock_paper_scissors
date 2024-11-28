import re
from unittest.mock import patch

import pytest
from core.classes.game import Game
from tests.tests_app.utils.utils import (
    get_all_text,
    get_first_second,
    safe_to_execute_game,
)


@pytest.mark.game_tests
@pytest.mark.parametrize(
    "choice_1, choice_2, expected_result",
    [
        ("камень", "ножницы", "выиграл"),
        ("камень", "камень", "ничья"),
        ("камень", "бумага", "проиграл"),
    ],
)
def test_rules_game(
    game_app: Game,
    player_1_name: str,
    player_2_name: str,
    choice_1: str,
    choice_2: str,
    expected_result: str,
) -> None:
    """
    Проверяем категорию 'Статистика'.
    - При победе добавляется победа. А у противника добавляется поражение.
    - При поражении добавляется поражение. А у противника добавляется победа.
    - Если ничья - ничего не добавляется.

    :param game_app: Экземпляр класса Game.
    :param player_1_name: Имя игрока №1.
    :param player_2_name: Имя игрока №2.
    :param choice_1: Выбранный элемент игрока, чей ход 1-м.
    :param choice_2: Выбранный элемент игрока, чей ход 2-м.
    :param expected_result: Исход игры для игрока, чей ход 1-м.
    :return: None.
    """

    choice_data = {"камень": "1", "ножницы": "2", "бумага": "3"}

    # Сценарий: Выбираем количество игроков, игроки представляются,
    # начинаем игру, игроки выбирают элемент, смотрим статистику, выходим из игры.
    user_inputs = [
        "2",
        player_1_name,
        player_2_name,
        "1",
        choice_data[choice_1],
        choice_data[choice_2],
        "2",
        "3",
        "3",
    ]
    with (
        patch("builtins.input", side_effect=user_inputs) as mock_input,
        patch("builtins.print") as mock_print,
    ):

        safe_to_execute_game(game_app)
        input_text = get_all_text(mock_input)
        printed_text = get_all_text(mock_print)

    # Определим игрока, чей ход был первым.
    first_player, second_player = get_first_second(
        input_text, player_1_name, player_2_name
    )

    match expected_result:
        case "ничья":
            assert re.search(
                rf"{first_player}.+Побед: 0.+Поражений: 0[^*]+", printed_text
            )
            assert re.search(
                rf"{second_player}.+Побед: 0.+Поражений: 0[^*]+",
                printed_text,
            )
        case "выиграл":
            assert re.search(
                rf"{first_player}.+Побед: 1.+Поражений: 0[^*]+", printed_text
            )
            assert re.search(
                rf"{second_player}.+Побед: 0.+Поражений: 1[^*]+",
                printed_text,
            )
        case "проиграл":
            assert re.search(
                rf"{first_player}.+Побед: 0.+Поражений: 1[^*]+", printed_text
            )
            assert re.search(
                rf"{second_player}.+Побед: 1.+Поражений: 0[^*]+",
                printed_text,
            )
