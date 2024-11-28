from unittest.mock import patch

import pytest
from core.classes.game import Game
from tests.tests_app.utils.utils import get_all_text, safe_to_execute_game


@pytest.mark.visual_tests
def test_choice_elements_menu(game_app: Game, player_1_name: str) -> None:
    """
    Проверка меню выбора элементов:
    - Содержит все ожидаемые категории.
    - Категории идут в правильном порядке.
    - Нет лишних категорий.
    - Есть приглашение пользователю для выбора категории.

    :param game_app: Экземпляр класса Game.
    :param player_1_name: Имя игрока №1.
    :return: None.
    """

    # Сценарий: Выбираем количество игроков, игрок представляется, начинаем игру, выходим из игры.
    user_inputs = ["1", player_1_name, "1", "4", "3", "3"]

    with patch("builtins.input", side_effect=user_inputs) as mock_input, patch(
        "builtins.print"
    ) as mock_print:
        safe_to_execute_game(game_app)
        input_text = get_all_text(mock_input)
        printed_text = get_all_text(mock_print)

    assert "1. Камень." in printed_text
    assert "2. Ножницы." in printed_text
    assert "3. Бумага." in printed_text

    assert "4. Выход." in printed_text
    assert "5." not in printed_text

    assert f"Ход игрока: {player_1_name}. Сделайте Ваш выбор:" in input_text
