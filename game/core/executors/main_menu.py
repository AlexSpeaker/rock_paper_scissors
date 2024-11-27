from core.classes.game import Game, GameExit
from core.classes.player import Player
from core.menu import game_menu, main_menu


@main_menu.mark(name="Один игрок")
def one_player(game: Game) -> None:
    name = input("Введите ваше имя: ")
    game.player_1 = Player(name)
    game.player_2 = Player("Компьютер", computer=True)
    game_menu.set_game(game)
    game_menu.show()


@main_menu.mark(name="Два игрока")
def two_players(game: Game) -> None:
    name_1 = input("Игрок 1. Введите ваше имя: ")
    game.player_1 = Player(name_1)
    name_2 = input("Игрок 2. Введите ваше имя: ")
    game.player_2 = Player(name_2)
    game_menu.set_game(game)
    game_menu.show()


@main_menu.mark(name="Выйти из игры")
def exit_game(game: Game) -> None:
    raise GameExit
