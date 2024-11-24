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
    timeout = 5.0
    thread = threading.Thread(target=game.run)
    try:
        thread.start()
        thread.join(timeout)
    except SystemExit:
        pass
    if thread.is_alive():
        raise TimeoutException("Время выполнения превышено!")


def get_all_text(mock: MagicMock) -> str:
    """
    Преобразует все перехваты в строку.
    :param mock: Объект имитации (MagicMock).
    :return: Строку (str).
    """
    return " ".join(" ".join(map(str, call.args)) for call in mock.call_args_list)
