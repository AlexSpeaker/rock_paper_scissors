from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional, Tuple

if TYPE_CHECKING:
    from core.classes.menu import Menu
    from core.classes.player import Player


class NoPlayerGame(Exception):
    pass


class GameExit(Exception):
    pass


@dataclass(frozen=True)
class ResultGame:
    winner: Optional["Player"] = None
    loser: Optional["Player"] = None


class Game:
    """Класс игры."""

    def __init__(self, start_menu: "Menu"):
        self.__start_menu = start_menu
        self.__start_menu.set_game(self)
        self.__player_1: Optional["Player"] = None
        self.__player_2: Optional["Player"] = None
        self.__who_is_now: Optional["Player"] = None

    def get_players(self) -> Tuple["Player", "Player"]:
        if self.__player_1 is None or self.__player_2 is None:
            raise NoPlayerGame("В игре должно быть два игрока")
        return self.__player_1, self.__player_2

    @property
    def player_1(self) -> "Player":
        if self.__player_1 is None:
            raise NoPlayerGame("Игрок 1 не задан")
        return self.__player_1

    @player_1.setter
    def player_1(self, player: "Player") -> None:
        self.__player_1 = player

    @property
    def player_2(self) -> "Player":
        if self.__player_2 is None:
            raise NoPlayerGame("Игрок 2 не задан")
        return self.__player_2

    @player_2.setter
    def player_2(self, player: "Player") -> None:
        self.__player_2 = player

    @property
    def who_is_now(self) -> Optional["Player"]:
        return self.__who_is_now

    @who_is_now.setter
    def who_is_now(self, who_is_now: "Player") -> None:
        self.__who_is_now = who_is_now

    def run(self) -> None:
        while True:
            try:
                self.__start_menu.show()
            except GameExit:
                exit(0)
