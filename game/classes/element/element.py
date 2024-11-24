from typing import Optional

from classes.exception.exception import NoElementResist


class Element:
    """Класс элемента."""

    def __init__(self, name: str) -> None:
        """
        Инициализация экземпляра.
        """
        self.__name = name
        self.__resists_the_element: Optional[Element] = None

    @property
    def name(self) -> str:
        """
        Возвращает имя элемента.
        :return: Имя элемента (str).
        """
        return self.__name

    @property
    def resists_the_element(self) -> Optional["Element"]:
        """
        Возвращает элемент, к которому текущий элемент устойчив.
        :return: Экземпляр класса Element, если он задан, иначе None.
        """
        return self.__resists_the_element

    @resists_the_element.setter
    def resists_the_element(self, element: "Element") -> None:
        """
        Задаёт элемент, к которому текущий элемент устойчив.
        :param element: Экземпляр класса Element.
        :return: None.
        """
        if not isinstance(element, Element):
            raise ValueError(f"Ожидали Element, а получили {type(element)}")
        self.__resists_the_element = element

    def is_resists(self, other_element: "Element") -> Optional[bool]:
        """
        Проверяет, устойчив ли текущий элемент к переданному элементу.
        :param other_element: Экземпляр класса Element, с которым проводится сравнение.
        :return: True, если устойчивость есть, False, если нет устойчивости, а если элементы одинаковы вернёт None.
        """
        if self.resists_the_element is None:
            raise NoElementResist(
                f"У элемента '{self.name}' нет элемента к которому он устойчив."
            )
        if self is other_element:
            return None
        return self.resists_the_element is other_element

    def __repr__(self) -> str:
        """
        Возвращает строковое представление элемента для отладки.
        :return: Строковое представление элемента (str)
        """
        return f"Element(name={self.name})"
