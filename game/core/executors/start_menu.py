from core.classes.game import Game, NoPlayerGame
from core.classes.menu import MenuExit
from core.elements import paper, scissors, stone
from core.menu import start_menu


@start_menu.mark(name="Камень")
def stone_menu(game: Game) -> None:
    """
    Функция-исполнитель. Выполнится при выборе игроком категорию 'Камень'.
    Присвоит игроку элемент 'Камень'.

    :param game: Экземпляр класса Game.
    :return: None.
    """
    player = game.who_is_now
    if player is None:
        raise NoPlayerGame("Не задан игрок, чей сейчас ход.")
    player.element = stone


@start_menu.mark(name="Ножницы")
def scissors_menu(game: Game) -> None:
    """
    Функция-исполнитель. Выполнится при выборе игроком категорию 'Ножницы'.
    Присвоит игроку элемент 'Ножницы'.

    :param game: Экземпляр класса Game.
    :return: None.
    """
    player = game.who_is_now
    if player is None:
        raise NoPlayerGame("Не задан игрок, чей сейчас ход.")
    player.element = scissors


@start_menu.mark(name="Бумага")
def paper_menu(game: Game) -> None:
    """
    Функция-исполнитель. Выполнится при выборе игроком категорию 'Бумага'.
    Присвоит игроку элемент 'Бумага'.

    :param game: Экземпляр класса Game.
    :return: None.
    """
    player = game.who_is_now
    if player is None:
        raise NoPlayerGame("Не задан игрок, чей сейчас ход.")
    player.element = paper


@start_menu.mark(name="Выход")
def exit_menu(game: Game) -> None:
    """
    Функция-исполнитель. Выполнится при выборе игроком категорию 'Выход'.
    Выйдет из данного меню.

    :param game: Экземпляр класса Game.
    :return: None.
    """
    game.player_1.reset_element()
    game.player_2.reset_element()
    raise MenuExit
