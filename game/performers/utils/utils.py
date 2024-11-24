from typing import TYPE_CHECKING, Optional, Sequence

from classes.exception.exception import NoElement
from classes.player.player import Player

if TYPE_CHECKING:
    from classes.game.game import ResultGame


def result_game(game_result: Optional["ResultGame"]) -> None:
    """
    Оповещает игроков о результатах игры.
    :param game_result: Экземпляр дата-класса ResultGame, если есть победитель и проигравший, или None, если ничья.
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
    print(
        f"Игрок {player_loser.name} проиграл. Его выбор: {player_loser.element.name}."
    )


def reset_elements(players: Sequence[Player]) -> None:
    """
    Сбросит выбранные элементы у игроков.
    :param players: Последовательность из игроков (экземпляры класса Player).
    :return: None.
    """
    for player in players:
        player.reset_element()


def editing_statistics(game_result: "ResultGame") -> None:
    """
    Правит статистику игроков. Победителю добавляет победу, а проигравшему поражение.
    :param game_result: Экземпляр дата-класса ResultGame.
    :return: None.
    """
    game_result.winner.add_wins()
    game_result.loser.add_losses()


def players_statistics(players: Sequence[Player]) -> None:
    """
    Покажет игрокам их статистику.
    :param players: Последовательность из игроков (экземпляры класса Player).
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
