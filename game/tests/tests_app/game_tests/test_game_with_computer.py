import re
from unittest.mock import patch

import pytest
from core.classes.game import Game
from tests.tests_app.utils.utils import get_all_text, safe_to_execute_game


@pytest.mark.game_tests
def test_game_with_computer(game_app: Game, player_1_name: str) -> None:
    """
    Проверим, что компьютер выбирает элементы случайно. Проведём 333 теста.
    - Если компьютер выбирает по порядку, то каждый элемент будет выбран 111 раз. Это провал теста.
    - Если компьютер выбирает один и тот же элемент, то один из элементов будет выбран 333 раза. Это провал теста.
    Примечание:
    - В случае 'ничьи' результат выбора компьютера не выводится на экран, но мы знаем, что выбрал пользователь.
    - Так как мы имеем дело со случайностью, то 'звёзды' могут сойтись так,
      что компьютер может выбрать, как один элемент 333 раза, так и каждый элемент по 111 раз,
      но вероятность этого ничтожна мала. Если же это произошло, то стоит подумать над покупкой лотерейного билета.

    :param game_app: Экземпляр класса Game.
    :param player_1_name: Имя игрока №1.
    :return:
    """

    computer_choice = {"камень": 0, "ножницы": 0, "бумага": 0}
    number_of_iterations = 333

    for _ in range(number_of_iterations):
        # Сценарий: Выбираем количество игроков, игрок представляется,
        # начинаем игру, игрок выбирает элемент ('Камень'), выходим из игры.
        user_inputs = ["1", player_1_name, "1", "1", "3", "3"]

        with (
            patch("builtins.input", side_effect=user_inputs),
            patch("builtins.print") as mock_print,
        ):
            safe_to_execute_game(game_app)
            printed_text = get_all_text(mock_print).lower()
        if "ничья" in printed_text:
            computer_choice["камень"] += 1
        else:
            pattern = r"компьютер[^:]+:\s+\b([^\.]+)\."
            search_computer_choice_result_search = re.search(pattern, printed_text)
            if not search_computer_choice_result_search:
                raise AssertionError(
                    "Что-то пошло не так. Не найден элемент выбранный компьютером."
                )
            search_computer_choice = search_computer_choice_result_search.group(
                1
            ).strip()
            computer_choice[search_computer_choice] += 1
    assert all(
        count_choice != number_of_iterations
        for count_choice in computer_choice.values()
    )
    assert len(set(computer_choice.values())) != 1
