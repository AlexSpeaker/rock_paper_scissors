import random
from dataclasses import dataclass
from typing import List, Optional

from classes.game.menu.category import BaseCategory
from classes.game.menu.menu import BaseGameMenu
from classes.player.player import Player
from performers.category import ExitGame, GameStatistics, StartGame


@dataclass(frozen=True)
class ResultGame:
    """
    Класс, куда будут записываться победитель и проигравший.
    """

    winner: Player
    loser: Player


class BaseGame:
    """
    Базовый класс игры.
    """

    def __init__(self, player_1: Player, player_2: Player) -> None:
        """
        Инициализация экземпляра.
        """
        self._player_1 = player_1
        self._player_2 = player_2
        self.__whose_move: Optional[Player] = None

    @property
    def player_1(self) -> Player:
        """
        Возвращает игрока под номером 1.
        :return: Экземпляр класса Player.
        """
        return self._player_1

    @property
    def player_2(self) -> Player:
        """
        Возвращает игрока под номером 2.
        :return: Экземпляр класса Player.
        """
        return self._player_2

    @property
    def players(self) -> List[Player]:
        """
        Возвращает список из игроков.
        :return: Список из экземпляров класса Player.
        """
        return [self.player_1, self.player_2]

    def who_is_walking(self) -> Player:
        """
        Возвращает игрока, который должен делать ход, если такой не задан, ф-ция случайным образом назначит такого.
        :return: Экземпляр класса Player.
        """
        if self.__whose_move is None:
            self.__whose_move = random.choice(self.players)
        return self.__whose_move

    def next_walker(self) -> None:
        """
        Сменит игрока, чей должен быть ход.
        :return: None
        """
        player = self.__whose_move
        if player is self.player_1:
            self.__whose_move = self.player_2
        else:
            self.__whose_move = self.player_1

    def reset_walker(self) -> None:
        """
        Сбросит информацию о том, чей сейчас ход на None.
        :return: None
        """
        self.__whose_move = None


class Game(BaseGame):
    """Класс игры"""

    def __init__(self, player_1: Player, player_2: Player) -> None:
        """
        Инициализация экземпляра.
        """
        super().__init__(player_1, player_2)
        self.__main_menu = GameMenu()

    def run(self) -> None:
        """
        Запуск функции запуска игры.
        :return: None
        """
        self.show_main_menu()

    def show_main_menu(self) -> None:
        """
        Запуск игры. Показывает игроку главное меню и выполнит его выбор.
        :return: None
        """
        while True:
            self.__main_menu.show()
            player_choice = input("Сделайте Ваш выбор: ").strip()
            choice_is_valid, message = self.__main_menu.valid_choice(player_choice)
            if choice_is_valid:
                self.__main_menu.execute(self, player_choice)
                continue
            else:
                print(message)

    def get_a_winner_and_loser(self) -> Optional[ResultGame]:
        """
        Определит победителя и проигравшего, а так же упакует их в дата-класс для удобной работы с ними в дальнейшем.
        :return: Экземпляр дата-класса ResultGame, если есть победитель и проигравший, иначе None.
        """
        if self.player_1.is_resists(self.player_2):
            return ResultGame(winner=self.player_1, loser=self.player_2)
        elif self.player_2.is_resists(self.player_1):
            return ResultGame(winner=self.player_2, loser=self.player_1)
        else:
            return None


class GameMenu(BaseGameMenu[BaseCategory]):
    """
    Класс главного меню.
    """

    game_menu = [
        StartGame(),
        GameStatistics(),
        ExitGame(),
    ]
