import threading
from unittest.mock import MagicMock

from classes.game.game import Game


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
