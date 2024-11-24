from classes.game.menu.category import BaseCategory
from classes.game.menu.menu import BaseGameMenu
from performers.category import ChoicePaper, ChoiceScissors, ChoiceStone, ExitGame


class ChoiceMenu(BaseGameMenu[BaseCategory]):
    """
    Класс меню выбора элемента.
    """

    game_menu = [
        ChoiceStone(),
        ChoiceScissors(),
        ChoicePaper(),
        ExitGame(),
    ]
