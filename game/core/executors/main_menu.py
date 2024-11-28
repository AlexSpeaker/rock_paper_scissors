from core.classes.game import Game, GameExit
from core.classes.menu import MenuExit
from core.classes.player import Player
from core.menu import game_menu, main_menu


@main_menu.mark(name="Один игрок")
def one_player_menu(game: Game) -> None:
    name = input("Введите ваше имя: ")
    game.player_1 = Player(name)
    game.player_2 = Player("Компьютер", computer=True)
    game_menu.set_game(game)
    while True:
        try:
            game_menu.show()
        except MenuExit:
            break


@main_menu.mark(name="Два игрока")
def two_players_menu(game: Game) -> None:
    name_1 = input("Игрок 1. Введите ваше имя: ")
    game.player_1 = Player(name_1)
    name_2 = input("Игрок 2. Введите ваше имя: ")
    game.player_2 = Player(name_2)
    game_menu.set_game(game)
    while True:
        try:
            game_menu.show()
        except MenuExit:
            break


@main_menu.mark(name="Выйти из игры")
def exit_game_menu(game: Game) -> None:
    raise GameExit
