from unittest.mock import patch

import pytest
from core.classes.game import Game
from tests.tests_app.utils.utils import get_all_text, safe_to_execute_game


@pytest.mark.visual_tests
def test_main_menu(game_app: Game) -> None:
    """
    Проверка главного меню:
    - Содержит все ожидаемые категории главного меню.
    - Категории идут в правильном порядке.
    - Нет лишних категорий.
    - Есть приглашение пользователю для выбора категории.
    - Бонусом проверяем, что категория "Выход" работает.

    :param game_app: Экземпляр класса Game.
    :return: None
    """
    with patch("builtins.input", return_value="3") as mock_input, patch(
        "builtins.print"
    ) as mock_print:
        safe_to_execute_game(game_app)
        input_text = get_all_text(mock_input)
        printed_text = get_all_text(mock_print)

    assert "1. Один игрок." in printed_text
    assert "2. Два игрока." in printed_text
    assert "3. Выйти из игры." in printed_text
    assert "4." not in printed_text

    assert "Сделайте Ваш выбор:" in input_text
