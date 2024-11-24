from unittest.mock import patch

from classes.game.game import Game
from tests.tests_app.utils.utils import get_all_text, safe_to_execute_game


def test_choice_elements_menu(game_one_player: Game) -> None:
    """
    Проверка меню выбора элементов:
    - Содержит все ожидаемые категории.
    - Нет лишних категорий.
    - Есть приглашение пользователю для выбора категории.

    :param game_one_player: Экземпляр класса Game.
    :return: None
    """

    # Сценарий: Пользователь начинает игру.
    user_inputs = ["1"]

    with patch("builtins.input", side_effect=user_inputs) as mock_input, patch(
        "builtins.print"
    ) as mock_print:
        safe_to_execute_game(game_one_player)
        input_text = get_all_text(mock_input)
        printed_text = get_all_text(mock_print)

    assert "Камень." in printed_text
    assert "Ножницы." in printed_text
    assert "Бумага." in printed_text

    assert "4. Выход." in printed_text
    assert "5." not in printed_text

    assert input_text.count("Сделайте Ваш выбор:") == 2
