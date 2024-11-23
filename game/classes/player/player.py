from typing import Optional

from classes.element.element import Element


class BasePlayer:
    """Базовый класс игрока."""

    def __init__(self, player_name: str, computer: bool = False) -> None:
        """
        Инициализация экземпляра.
        """
        if not player_name:
            raise ValueError("Имя игрока не может быть пустым.")
        self.__player_name = player_name
        self.__computer = computer

    @property
    def name(self) -> str:
        """
        Возвращает имя игрока.
        :return: Имя игрока (str).
        """
        return self.__player_name

    @property
    def is_computer(self) -> bool:
        """
        Возвращает True, если игрок — компьютер.
        :return: True, если игрок компьютер, иначе False.
        """
        return self.__computer


class BasePlayerStatistics:
    """Класс для хранения статистики игрока."""

    def __init__(self) -> None:
        """
        Инициализация экземпляра.
        """
        self.__number_of_wins = 0
        self.__number_of_losses = 0

    @property
    def wins(self) -> int:
        """
        Количество побед игрока.
        :return: Количество побед игрока (int).
        """
        return self.__number_of_wins

    @property
    def losses(self) -> int:
        """
        Количество поражений игрока.
        :return: Количество поражений игрока (int).
        """
        return self.__number_of_losses

    def add_wins(self) -> None:
        """
        Добавляет победу игроку.
        :return: None
        """
        self.__number_of_wins += 1

    def add_losses(self) -> None:
        """
        Добавляет поражение игроку.
        :return: None
        """
        self.__number_of_losses += 1


class BasePlayerElement:
    """Класс для работы с элементом игрока."""

    def __init__(self) -> None:
        """
        Инициализация экземпляра.
        """
        self.__element: Optional[Element] = None

    @property
    def element(self) -> Optional[Element]:
        """
        Текущий элемент игрока.
        :return: Экземпляр класса Element, если такой задан, иначе None.
        """
        return self.__element

    @element.setter
    def element(self, element: Element) -> None:
        """
        Задаёт элемент игроку.
        :param element: Экземпляр класса Element.
        :return: None
        """
        if not isinstance(element, Element):
            raise ValueError("Элемент должен быть экземпляром класса Element.")
        self.__element = element

    def reset_element(self) -> None:
        """
        Сбрасывает текущий элемент игрока.
        :return: None
        """
        self.__element = None


class Player(BasePlayer, BasePlayerStatistics, BasePlayerElement):
    """Класс игрока, объединяющий базовый функционал, статистику и элементы."""

    def __init__(self, player_name: str, computer: bool = False) -> None:
        """
        Инициализация экземпляра.
        """
        BasePlayer.__init__(self, player_name, computer)
        BasePlayerStatistics.__init__(self)
        BasePlayerElement.__init__(self)

    def is_resists(self, player: "Player") -> Optional[bool]:
        """
        Проверяет, устойчив ли текущий элемент игрока к элементу другого игрока.
        :param player: Экземпляр класса Player (другой игрок).
        :return: True, если текущий элемент устойчив, False, если текущий элемент не устойчив, None, если элементы одинаковы.
        """
        if self.element is None or player.element is None:
            raise ValueError("У одного из игроков не задан элемент.")
        return self.element.is_resists(player.element)

    def __repr__(self) -> str:
        """
        Строковое представление игрока для отладки.
        :return: Строковое представление игрока (str).
        """
        element = self.element.name if self.element else "None"
        return (
            f"Player(name={self.name}, computer={self.is_computer}, element={element})"
        )
