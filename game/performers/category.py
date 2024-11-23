import random
from typing import TYPE_CHECKING, List, Optional

from classes.element.elements import paper, scissors, stone
from classes.exception.exception import NoElement
from classes.game.menu.category import BaseCategory
from classes.game.menu.menu import BaseGameMenu
from classes.player.player import Player

if TYPE_CHECKING:
    from classes.game.game import Game, ResultGame


class StartGame(BaseCategory):
    """Класс категории меню 'Начать игру'."""

    name_category = "Начать игру."

    def __init__(self) -> None:
        """
        Инициализация экземпляра.
        """
        super().__init__()
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
        self.__result_game(game_result)
        game.reset_walker()

    @staticmethod
    def __result_game(game_result: Optional["ResultGame"]) -> None:
        """
        Оповещает игроков о результатах игры, правит статистику и сбросит их выбранные элементы.
        :param game_result: Экземпляр дата-класса ResultGame.
        :return: None
        """
        if game_result is None:
            print("НИЧЬЯ!")
            return
        player_winner = game_result.winner
        player_loser = game_result.loser
        if not player_winner.element or not player_loser.element:
            raise NoElement(
                f"У одного из игроков нет элемента. "
                f"У игрока {player_winner.name} элемент "
                f"{player_winner.element.name if player_winner.element else 'None'}. "
                f"У игрока {player_loser.name} элемент "
                f"{player_loser.element.name if player_loser.element else 'None'}"
            )
        print(
            f"Игрок {player_winner.name} ПОБЕДИЛ!!! Его выбор: {player_winner.element.name}."
        )
        player_winner.add_wins()
        player_winner.reset_element()
        print(
            f"Игрок {player_loser.name} проиграл. Его выбор: {player_loser.element.name}."
        )
        player_loser.add_losses()
        player_loser.reset_element()

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
            player_choice = input(f"{player.name}, Сделайте Ваш выбор: ").strip()
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
        self.get_players_statistics(game.players)

    @staticmethod
    def get_players_statistics(players: List[Player]) -> None:
        """
        Покажет игрокам их статистику.
        :param players: Список игроков (экземпляры класса Player).
        :return: None.
        """
        width_menu = 26
        print("*" * width_menu)
        for i, player in enumerate(players, 1):
            print(
                "*{:^{width_menu}}*".format(
                    f"{i}. {player.name}", width_menu=width_menu - 2
                )
            )
            print(
                "*{:^{width_menu}}*".format(
                    f"Побед: {player.wins}", width_menu=width_menu - 2
                )
            )
            print(
                "*{:^{width_menu}}*".format(
                    f"Поражений: {player.losses}", width_menu=width_menu - 2
                )
            )
            if i != len(players):
                print(
                    "*{:^{width_menu}}*".format(
                        "-" * (width_menu - 2), width_menu=width_menu - 2
                    )
                )
        print("*" * width_menu)


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

    name_category = "Камень"

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

    name_category = "Бумага"

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

    name_category = "Ножницы"

    def execute(self, game: "Game") -> None:
        """
        Запуск категории 'Ножницы'. Присвоит текущему игроку элемент 'Ножницы'.
        :param game: Экземпляр класса Game.
        :return: None
        """
        player = game.who_is_walking()
        player.element = scissors


class ChoiceMenu(BaseGameMenu[BaseCategory]):
    """
    Класс меню выбора элемента.
    """

    game_menu = [
        ChoiceStone(),
        ChoiceScissors(),
        ChoicePaper(),
        ExitGame(),
    ]
