from unittest.mock import patch

import pytest
from classes.game.game import Game
from classes.player.player import Player
from tests.tests_app.utils.utils import get_all_text, safe_to_execute_game


@pytest.mark.parametrize(
    "human_player_choice, another_human_player_choice, expected_result",
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
    game_two_player: Game,
    human_player: Player,
    another_human_player: Player,
    human_player_choice: str,
    another_human_player_choice: str,
    expected_result: str,
) -> None:
    """
    Проверяем правила игры.
    Бонусом проверяем вывод.

    :param game_two_player: Экземпляр класса Game.
    :param human_player: 1-й игрок (Экземпляр класса Player).
    :param another_human_player: 2-й игрок (Экземпляр класса Player).
    :param human_player_choice: Выбранный элемент 1-го игрока (str).
    :param another_human_player_choice: Выбранный элемент 2-го игрока (str).
    :param expected_result: Как должна закончится игра для 1-го игрока.
    :return: None
    """
    choice_data = {"камень": "1", "ножницы": "2", "бумага": "3"}

    # Сценарий: Пользователь начинает игру. Пользователи по очереди выбирают элемент.
    user_inputs = [
        "1",
        choice_data[human_player_choice],
        choice_data[another_human_player_choice],
    ]

    with (
        patch("builtins.input", side_effect=user_inputs) as mock_input,
        patch("builtins.print") as mock_print,
    ):

        safe_to_execute_game(game_two_player)
        input_text = get_all_text(mock_input)
        printed_text = get_all_text(mock_print).lower()

    match expected_result:

        case "ничья":
            assert "ничья".lower() in printed_text
        case "выиграл":
            assert (
                f"Игрок {human_player.name} ПОБЕДИЛ!!! Его выбор: {human_player_choice}.".lower()
                in printed_text
            )
            assert (
                f"Игрок {another_human_player.name} проиграл. Его выбор: {another_human_player_choice}.".lower()
                in printed_text
            )
        case "проиграл":
            assert (
                f"Игрок {another_human_player.name} ПОБЕДИЛ!!! Его выбор: {another_human_player_choice}.".lower()
                in printed_text
            )
            assert (
                f"Игрок {human_player.name} проиграл. Его выбор: {human_player_choice}.".lower()
                in printed_text
            )

    assert f"Ход игрока: {human_player.name}. Сделайте Ваш выбор:" in input_text
    assert f"Ход игрока: {another_human_player.name}. Сделайте Ваш выбор:" in input_text
