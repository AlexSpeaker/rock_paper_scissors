from core.classes.game import Game
from core.classes.menu import ExitMenu
from core.classes.player import Player
from core.menu import main_menu, game_menu


@main_menu.mark(name="Один игрок")
def one_player(game: Game) -> None:
    name = input("Введите ваше имя: ")
    game.player_1 = Player(name)
    game.player_2 = Player("Компьютер", computer=True)
    game_menu.set_game(game)
    game_menu.show()


@main_menu.mark(name="Два игрока")
def two_players(game: Game) -> None:
    pass


@main_menu.mark(name="Выйти из игры")
def exit_game(game: Game) -> None:
    raise ExitMenu
