from classes.game_class import Game
from classes.player_class import Player

if __name__ == "__main__":

    player_computer = Player(player_name="Компьютер", computer=True)
    name_player_human = input("Введите Ваше имя: ")
    player_human = Player(player_name=name_player_human)

    game = Game(player_1=player_computer, player_2=player_human)
    game.game_run()
