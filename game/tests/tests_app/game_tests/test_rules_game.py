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
        ("ножницы", "бумага", "выиграл"),
        ("бумага", "камень", "выиграл"),
        ("камень", "камень", "ничья"),
        ("ножницы", "ножницы", "ничья"),
        ("бумага", "бумага", "ничья"),
        ("камень", "бумага", "проиграл"),
        ("ножницы", "камень", "проиграл"),
        ("бумага", "ножницы", "проиграл"),
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
    Проверяем правила игры.
    Бонусом проверяем вывод.

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
    # начинаем игру, игроки выбирают элемент, выходим из игры.
    user_inputs = [
        "2",
        player_1_name,
        player_2_name,
        "1",
        choice_data[choice_1],
        choice_data[choice_2],
        "3",
        "3",
    ]

    with (
        patch("builtins.input", side_effect=user_inputs) as mock_input,
        patch("builtins.print") as mock_print,
    ):

        safe_to_execute_game(game_app)
        input_text = get_all_text(mock_input)
        printed_text = get_all_text(mock_print).lower()

    # Определим игрока, чей ход был первым.
    first_player, second_player = get_first_second(
        input_text, player_1_name, player_2_name
    )

    match expected_result:
        case "ничья":
            assert "ничья".lower() in printed_text
        case "выиграл":
            assert (
                f"Игрок {first_player} ПОБЕДИЛ!!! Его выбор: {choice_1}.".lower()
                in printed_text
            )
            assert (
                f"Игрок {second_player} проиграл. Его выбор: {choice_2}.".lower()
                in printed_text
            )
        case "проиграл":
            assert (
                f"Игрок {second_player} ПОБЕДИЛ!!! Его выбор: {choice_2}.".lower()
                in printed_text
            )
            assert (
                f"Игрок {first_player} проиграл. Его выбор: {choice_1}.".lower()
                in printed_text
            )

    assert f"Ход игрока: {player_1_name}. Сделайте Ваш выбор:" in input_text
    assert f"Ход игрока: {player_2_name}. Сделайте Ваш выбор:" in input_text
