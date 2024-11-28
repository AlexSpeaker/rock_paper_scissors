from random import choice

from core.classes.element import NoElementExists
from core.classes.game import Game, GameExit, ResultGame
from core.classes.menu import MenuExit
from core.classes.player import Player
from core.elements import paper, scissors, stone
from core.menu import game_menu, start_menu


def statistics_info(player: Player, index: int, width_menu: int) -> None:
    print("*" * width_menu)
    print(
        "*{:^{width_menu}}*".format(
            f"{index}. {player.name}", width_menu=width_menu - 2
        )
    )
    print(
        "*{:^{width_menu}}*".format(f"Побед: {player.wins}", width_menu=width_menu - 2)
    )
    print(
        "*{:^{width_menu}}*".format(
            f"Поражений: {player.losses}", width_menu=width_menu - 2
        )
    )
    print("*" * width_menu)


@game_menu.mark(name="Начать игру")
def start_game_menu(game: Game) -> None:
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
    players = game.get_players()
    max_width = max((player.name for player in players), key=len)
    width_menu = len(max_width) + 15
    for i, player in enumerate(players):
        statistics_info(player, i, width_menu)


@game_menu.mark(name="Выход")
def exit_menu(game: Game) -> None:
    raise MenuExit


def get_result_game(game: Game) -> ResultGame:
    player_1, player_2 = game.get_players()
    if player_1.is_resists(player_2):
        return ResultGame(winner=player_1, loser=player_2)
    elif player_2.is_resists(player_1):
        return ResultGame(winner=player_2, loser=player_1)
    return ResultGame()


def game_summary(result_game: ResultGame) -> None:
    if result_game.winner and result_game.loser:
        if not result_game.winner.element:
            raise NoElementExists("У победителя внезапно пропал элемент.")
        if not result_game.loser.element:
            raise NoElementExists("У проигравшего внезапно пропал элемент.")

        print(
            f"Игрок {result_game.winner.name} ПОБЕДИЛ! Его выбор: {result_game.winner.element.name}."
        )
        result_game.winner.add_wins()

        print(
            f"Игрок {result_game.loser.name} проиграл! Его выбор: {result_game.loser.element.name}."
        )
        result_game.loser.add_losses()

    else:
        print("НИЧЬЯ.")
