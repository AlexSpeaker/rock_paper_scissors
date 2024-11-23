from classes.game.game import Game
from classes.player.player import Player

"""
Задаём игроков и запускаем игру.
"""

if __name__ == "__main__":
    player_computer = Player(player_name="Компьютер", computer=True)
    name_player_human = input("Введите Ваше имя: ")
    player_human = Player(player_name=name_player_human)
    game = Game(player_human, player_computer)
    game.run()
