from core.classes.game import Game
from core.menu import game_menu


@game_menu.mark(name="Начать игру")
def start_game(game: Game):
    pass
@game_menu.mark(name="Статистика")
def statistic(game: Game):
    pass
@game_menu.mark(name="Выход")
def exit_menu(game: Game):
    pass