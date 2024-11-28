from core.classes.element import NoElementExists
from core.classes.game import Game, ResultGame
from core.classes.player import Player


def statistics_info(player: Player, index: int, width_menu: int) -> None:
    """
    Функция покажет статистику игрока.

    :param player: Игрок.
    :param index: Порядковый номер игрока.
    :param width_menu: Размер рамки.
    :return:
    """
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


def get_result_game(game: Game) -> ResultGame:
    """
    Функция определит результат игры, и вернёт эту информацию, упакованную в ResultGame.

    :param game: Экземпляр игры.
    :return: Результат игры.
    """
    player_1, player_2 = game.get_players()
    if player_1.is_resists(player_2):
        return ResultGame(winner=player_1, loser=player_2)
    elif player_2.is_resists(player_1):
        return ResultGame(winner=player_2, loser=player_1)
    return ResultGame()


def game_summary(result_game: ResultGame) -> None:
    """
    Функция подведёт итог игры: покажет результаты и обновит статистику.

    :param result_game: Результат игры.
    :return: None.
    """
    if result_game.winner and result_game.loser:
        if not result_game.winner.element:
            raise NoElementExists("У победителя внезапно пропал элемент.")
        if not result_game.loser.element:
            raise NoElementExists("У проигравшего внезапно пропал элемент.")

        print(
            f"Игрок {result_game.winner.name} ПОБЕДИЛ!!! Его выбор: {result_game.winner.element.name}."
        )
        result_game.winner.add_wins()

        print(
            f"Игрок {result_game.loser.name} проиграл. Его выбор: {result_game.loser.element.name}."
        )
        result_game.loser.add_losses()

    else:
        print("НИЧЬЯ.")
