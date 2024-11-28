import re
import threading
from typing import Tuple
from unittest.mock import MagicMock

from core.classes.game import Game


class TimeoutException(Exception):
    """Класс-исключение превышения времени."""


def safe_to_execute_game(game: Game) -> None:
    """
    Безопасно запустит игру, а если она зависнет, то выдаст исключение.

    :param game: Экземпляр класса Game.
    :return: None.
    """

    def __game_run_function() -> None:
        try:
            game.run()
        except SystemExit:
            pass

    timeout = 5.0
    thread = threading.Thread(target=__game_run_function)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        raise TimeoutException("Время выполнения превышено!")


def get_all_text(mock: MagicMock) -> str:
    """
    Преобразует все перехваты в строку.

    :param mock: Объект имитации (MagicMock).
    :return: Строку (str).
    """
    return " ".join(" ".join(map(str, call.args)) for call in mock.call_args_list)


def get_first_second(
    input_text: str, player_1_name: str, player_2_name: str
) -> Tuple[str, str]:
    """
    Функция определяет и возвращает кортеж имён игроков, совершивших ходы в порядке их выполнения.
    :param input_text: История ходов.
    :param player_1_name: Имя игрока №1.
    :param player_2_name: Имя игрока №2.
    :return: Кортеж имён игроков, совершивших ходы в порядке их выполнения.
    """
    pattern = r"Ход игрока: ([^\.]+)\."
    name_first_player_result_search = re.search(pattern, input_text)
    if not name_first_player_result_search:
        raise AssertionError(
            "Что-то пошло не так, не найден игрок сделавший первый ход."
        )
    name_first_player = name_first_player_result_search.group(1)
    if player_1_name == name_first_player:
        first_player = player_1_name
        second_player = player_2_name
    else:
        first_player = player_2_name
        second_player = player_1_name

    return first_player, second_player
