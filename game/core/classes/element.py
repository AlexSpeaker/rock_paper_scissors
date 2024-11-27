from typing import Optional


class NoElementExists(Exception):
    pass


class Element:
    """Класс элемента."""

    def __init__(self, name: str) -> None:
        """
        Инициализация экземпляра.
        """
        if not name:
            raise ValueError("Имя элемента не может быть пустым.")
        self.__name = name
        self.__resists_element: Optional["Element"] = None

    @property
    def name(self) -> str:
        """
        Возвращает имя элемента.
        :return: Имя элемента (str).
        """
        return self.__name

    @property
    def resists_element(self) -> "Element":
        """
        Возвращает элемент, к которому текущий элемент устойчив.
        :return: Экземпляр класса Element.
        """
        if self.__resists_element is None:
            raise NoElementExists("У элемента нет элемента к которому он устойчив.")
        return self.__resists_element

    @resists_element.setter
    def resists_element(self, element: "Element") -> None:
        if self.__resists_element is not None:
            raise ValueError("Элементу уже задан элемент к которому он устойчив.")
        self.__resists_element = element

    def is_resists(self, other_element: "Element") -> Optional[bool]:
        """
        Проверяет, устойчив ли текущий элемент к переданному элементу.
        :param other_element: Экземпляр класса Element, с которым проводится сравнение.
        :return: True, если устойчивость есть, False, если нет устойчивости, а если элементы одинаковы вернёт None.
        """
        if not isinstance(other_element, Element):
            raise ValueError(
                f"Ожидали {type(Element)}, а получили {type(other_element)}."
            )
        if self is other_element:
            return None
        elif self.resists_element is other_element:
            return True
        return False

    def __repr__(self) -> str:
        """
        Возвращает строковое представление элемента для отладки.
        :return: Строковое представление элемента (str)
        """
        return f"Element(name={self.name}, resists_element={self.resists_element})"
