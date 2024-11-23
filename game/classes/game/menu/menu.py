from typing import TYPE_CHECKING, Generic, List, Tuple, TypeVar

from classes.game.menu.category import BaseCategory

C = TypeVar("C", bound=BaseCategory)
if TYPE_CHECKING:
    from classes.game.game import Game


class BaseGameMenu(Generic[C]):
    """Базовый класс для меню."""

    game_menu: List[C]

    def __init__(self) -> None:
        """
        Инициализация экземпляра.
        """
        self.__menu = self.game_menu

    @property
    def menu(self) -> List[C]:
        """
        Возвращает список из категорий меню.
        :return: Список из экземпляров-наследников BaseCategory.
        """
        return self.__menu

    def show(self) -> None:
        """
        Выводит на экран красивое меню.
        :return: None
        """
        width_menu = 26
        print("*" * width_menu)
        for i, category in enumerate(self.menu, 1):
            print(
                "*{:^{width_menu}}*".format(
                    f"{i}. {category.name}", width_menu=width_menu - 2
                )
            )
        print("*" * width_menu)

    def valid_choice(self, choice: str) -> Tuple[bool, str]:
        """
        Проверит правильно ли ввёл категорию пользователь при выборе категории.
        :param choice: Выбор пользователя (str)
        :return: (True, 'OK') если всё хорошо, иначе (True, 'Информация пользователю, что он не так делает').
        """
        try:
            choice_int = int(choice)
        except ValueError:
            return False, "Вводить нужно только цифры!"
        if choice_int < 1 or choice_int > len(self.menu):
            return False, "Вне диапазона меню!"
        return True, "OK"

    def execute(self, game: "Game", choice: str) -> None:
        """
        Выполнит выбранную пользователем категорию.
        :param game: Экземпляр класса Game.
        :param choice: Выбор пользователя. (Выбор нужно предварительно проверить через функцию valid_choice)
        :return: None
        """
        self.menu[int(choice) - 1].execute(game)
