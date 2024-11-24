import random
from typing import TYPE_CHECKING

from classes.game.menu.category import BaseCategory
from performers.utils.elements import paper, scissors, stone
from performers.utils.utils import (
    editing_statistics,
    players_statistics,
    reset_elements,
    result_game,
)

if TYPE_CHECKING:
    from classes.game.game import Game


class StartGame(BaseCategory):
    """Класс категории меню 'Начать игру'."""

    name_category = "Начать игру."

    def __init__(self) -> None:
        """
        Инициализация экземпляра.
        """
        super().__init__()
        from performers.utils.additional_menus import ChoiceMenu

        self.__menu = ChoiceMenu()

    def execute(self, game: "Game") -> None:
        """
        Запуск категории 'Начать игру'.
        :param game: Экземпляр класса Game.
        :return: None.
        """
        for _ in range(2):
            self.__step_game(game)
            game.next_walker()
        game_result = game.get_a_winner_and_loser()
        if game_result:
            editing_statistics(game_result)
        result_game(game_result)
        reset_elements(game.players)
        game.reset_walker()

    def __step_game(self, game: "Game") -> None:
        """
        Шаг игры.
        :param game: Экземпляр класса Game.
        :return: None.
        """
        while True:
            player = game.who_is_walking()
            if player.is_computer:
                player.element = random.choice([paper, stone, scissors])
                break
            self.__menu.show()
            player_choice = input(
                f"Ход игрока: {player.name}. Сделайте Ваш выбор: "
            ).strip()
            choice_is_valid, message = self.__menu.valid_choice(player_choice)
            if choice_is_valid:
                self.__menu.execute(game, player_choice)
                break
            else:
                print(message)


class GameStatistics(BaseCategory):
    """Класс категории меню 'Статистика'."""

    name_category = "Статистика."

    def execute(self, game: "Game") -> None:
        """
        Запуск категории 'Статистика'.
        :param game: Экземпляр класса Game.
        :return: None.
        """
        players_statistics(game.players)


class ExitGame(BaseCategory):
    """Класс категории меню 'Выход'."""

    name_category = "Выход."

    def execute(self, game: "Game") -> None:
        """
        Запуск категории 'Выход'. Завершит игру.
        :param game: Экземпляр класса Game.
        :return: None
        """
        exit(0)


class ChoiceStone(BaseCategory):
    """Класс категории меню 'Камень'."""

    name_category = "Камень."

    def execute(self, game: "Game") -> None:
        """
        Запуск категории 'Камень'. Присвоит текущему игроку элемент 'Камень'.
        :param game: Экземпляр класса Game.
        :return: None
        """
        player = game.who_is_walking()
        player.element = stone


class ChoicePaper(BaseCategory):
    """Класс категории меню 'Бумага'."""

    name_category = "Бумага."

    def execute(self, game: "Game") -> None:
        """
        Запуск категории 'Бумага'. Присвоит текущему игроку элемент 'Бумага'.
        :param game: Экземпляр класса Game.
        :return: None
        """
        player = game.who_is_walking()
        player.element = paper


class ChoiceScissors(BaseCategory):
    """Класс категории меню 'Ножницы'."""

    name_category = "Ножницы."

    def execute(self, game: "Game") -> None:
        """
        Запуск категории 'Ножницы'. Присвоит текущему игроку элемент 'Ножницы'.
        :param game: Экземпляр класса Game.
        :return: None
        """
        player = game.who_is_walking()
        player.element = scissors
