from random import choice

from core.classes.game import Game
from core.classes.menu import MenuExit
from core.elements import paper, scissors, stone
from core.executors.utils.utils import game_summary, get_result_game, statistics_info
from core.menu import game_menu, start_menu


@game_menu.mark(name="Начать игру")
def start_game_menu(game: Game) -> None:
    """
    Функция-исполнитель. Выполнится при выборе игроком категорию 'Начать игру'.
    Попросит игроков выбрать элемент.

    :param game: Экземпляр класса Game.
    :return: None.
    """
    game.player_1.reset_element()
    game.player_2.reset_element()
    start_menu.set_game(game)
    players = game.get_players()
    for i, player in enumerate(players):
        game.who_is_now = player
        if player.is_computer():
            player.element = choice([stone, scissors, paper])
            continue
        start_menu.set_message(f"Ход игрока: {player.name}. Сделайте Ваш выбор: ")
        if i and not player.is_computer():
            print("\n" * 25)
        try:
            start_menu.show()
        except MenuExit:
            break
    else:
        game_summary(get_result_game(game))


@game_menu.mark(name="Статистика")
def statistic_menu(game: Game) -> None:
    """
    Функция-исполнитель. Выполнится при выборе игроком категорию 'Статистика'.
    Покажет статистику по каждому игроку.

    :param game: Экземпляр класса Game.
    :return: None.
    """
    players = game.get_players()
    max_width = max((player.name for player in players), key=len)
    width_menu = len(max_width) + 15
    for i, player in enumerate(players, 1):
        statistics_info(player, i, width_menu)


@game_menu.mark(name="Выход")
def exit_menu(game: Game) -> None:
    """
    Функция-исполнитель. Выполнится при выборе игроком категорию 'Выход'.
    Выйдет из данного меню.

    :param game: Экземпляр класса Game.
    :return: None.
    """
    raise MenuExit
