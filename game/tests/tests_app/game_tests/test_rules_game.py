import re
from unittest.mock import patch

import pytest
from classes.game.game import Game
from classes.player.player import Player
from tests.tests_app.utils.utils import get_all_text, safe_to_execute_game


@pytest.mark.game_tests
@pytest.mark.parametrize(
    "player_choice, another_player_choice, expected_result",
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
    player_choice: str,
    another_player_choice: str,
    expected_result: str,
) -> None:
    """
    Проверяем правила игры.
    Бонусом проверяем вывод.

    :param game_two_player: Экземпляр класса Game.
    :param human_player: 1-й игрок (Экземпляр класса Player).
    :param another_human_player: 2-й игрок (Экземпляр класса Player).
    :param player_choice: Выбранный элемент игрока, сделавшего первый ход (str).
    :param another_player_choice: Выбранный элемент 2-го ходящего игрока (str).
    :param expected_result: Как должна закончится игра для игрока сделавшего 1-й ход.
    :return: None
    """
    choice_data = {"камень": "1", "ножницы": "2", "бумага": "3"}

    # Сценарий: Пользователь начинает игру. Игроки по очереди выбирают элемент. Выход из игры.
    user_inputs = [
        "1",
        choice_data[player_choice],
        choice_data[another_player_choice],
        "3",
    ]

    with (
        patch("builtins.input", side_effect=user_inputs) as mock_input,
        patch("builtins.print") as mock_print,
    ):

        safe_to_execute_game(game_two_player)
        input_text = get_all_text(mock_input)
        printed_text = get_all_text(mock_print).lower()

    # Определим игрока, чей ход был первым.
    pattern = r"Ход игрока: ([^\.]+)\."
    name_first_player_result_search = re.search(pattern, input_text)
    if not name_first_player_result_search:
        raise AssertionError(
            "Что-то пошло не так, не найден игрок сделавший первый ход."
        )
    name_first_player = name_first_player_result_search.group(1)
    if human_player.name == name_first_player:
        first_player = human_player
        second_player = another_human_player
    else:
        first_player = another_human_player
        second_player = human_player

    match expected_result:
        case "ничья":
            assert "ничья".lower() in printed_text
        case "выиграл":
            assert (
                f"Игрок {first_player.name} ПОБЕДИЛ!!! Его выбор: {player_choice}.".lower()
                in printed_text
            )
            assert (
                f"Игрок {second_player.name} проиграл. Его выбор: {another_player_choice}.".lower()
                in printed_text
            )
        case "проиграл":
            assert (
                f"Игрок {second_player.name} ПОБЕДИЛ!!! Его выбор: {another_player_choice}.".lower()
                in printed_text
            )
            assert (
                f"Игрок {first_player.name} проиграл. Его выбор: {player_choice}.".lower()
                in printed_text
            )

    assert f"Ход игрока: {human_player.name}. Сделайте Ваш выбор:" in input_text
    assert f"Ход игрока: {another_human_player.name}. Сделайте Ваш выбор:" in input_text
