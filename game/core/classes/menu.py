from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, Dict, List, Optional, Tuple

if TYPE_CHECKING:
    from core.classes.game import Game


class NoGameClass(Exception):
    """Исключение, если не нашёлся экземпляр игры."""


class NoFunction(Exception):
    """Исключение, если у категории отсутствует исполняющая функция."""


class MenuExit(Exception):
    """Исключение, для выхода из меню."""


@dataclass
class Func:
    """Класс содержит информацию об исполняющей функции категории и видимость этой категории."""

    func: Optional[Callable[["Game"], None]] = None
    hidden: bool = True


class Menu:
    """Класс меню категорий"""

    def __init__(self, *args: str) -> None:
        """
        Инициализация класса Menu.

        :param args: Перечень категорий меню. В этом же порядке они будут выводиться на экран.
        """
        self.__menu = list(args)
        self.__game: Optional["Game"] = None
        self.__message = "Сделайте Ваш выбор: "
        self.__menu_dict: Dict[str, Func] = {}

    def mark(
        self, name: str, hidden: bool = False
    ) -> Callable[[Callable[["Game"], None]], Callable[["Game"], None]]:
        """
        Декоратор регистрирующий функции, для категорий меню.

        :param name: Название категории меню.
        :param hidden: Скрытая ли это категория.
        :return: Callable[[Callable[[Game], None]], Callable[[Game], None]]
        """

        def decorator(func: Callable[["Game"], None]) -> Callable[["Game"], None]:
            self.__menu_dict[name] = Func(func, hidden)
            return func

        return decorator

    def set_game(self, game: "Game") -> None:
        """
        Передаёт меню экземпляр класса Game.

        :param game: Экземпляр класса Game.
        :return: None
        """
        self.__game = game

    def set_message(self, message: str) -> None:
        """
        Задаёт сообщение, которое будет показано пользователю при выборе категории.
        По умолчанию - это 'Сделайте Ваш выбор: '.

        :param message: Сообщение (str).
        :return: None
        """
        self.__message = message

    def show(self) -> None:
        """
        Покажет меню и будет ждать ответа от пользователя.
        Если выбор валидный выполнит соответствующую функцию.

        :return: None
        """
        if self.__game is None:
            raise NoGameClass(
                "В меню не нашлось экземпляра игры. Воспользуйтесь методом 'set_game'"
            )
        while True:
            self.__show_menu()
            choice_player = input(f"{self.__message}")
            result_validate, message = self.__validate_choice(choice_player)
            if not result_validate:
                print(message)
                continue
            break
        menu = self.__get_enabled_menu()
        func = self.__menu_dict[menu[int(choice_player) - 1]].func
        if not func:
            raise NoFunction(
                f"Не нашлось зарегистрированной функции для категории {menu[int(choice_player) - 1]}"
            )
        func(self.__game)

    def __get_enabled_menu(self) -> List[str]:
        """
        Вернёт список категорий меню, которые не спрятаны.

        :return: Список категорий List[str].
        """
        return [menu for menu in self.__menu if not self.__menu_dict[menu].hidden]

    def __show_menu(self) -> None:
        """
        Покажет красивое меню.

        :return: None
        """
        menu = self.__get_enabled_menu()
        max_width = max(menu, key=len)
        width_menu = len(max_width) + 15
        print("*" * width_menu)
        for i, category in enumerate(menu, 1):

            print(
                "*{:^{width_menu}}*".format(
                    f"{i}. {category}.", width_menu=width_menu - 2
                )
            )
        print("*" * width_menu)

    def __validate_choice(self, choice: str) -> Tuple[bool, str]:
        """
        Проверит правильно ли ввёл категорию пользователь при выборе категории.

        :param choice: Выбор пользователя (str)
        :return: (True, 'OK') если всё хорошо, иначе (True, 'Информация пользователю, что он не так делает').
        """
        try:
            choice_int = int(choice)
        except ValueError:
            return False, "Вводить нужно только цифры!"
        if choice_int < 1 or choice_int > len(self.__get_enabled_menu()):
            return False, "Вне диапазона меню!"
        return True, "OK"
