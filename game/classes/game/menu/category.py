from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.game.game import Game


class BaseCategory(ABC):
    """Базовый абстрактный класс категории меню."""

    name_category: str

    def __init__(self) -> None:
        """
        Инициализация экземпляра.
        """
        self._name = self.name_category

    @abstractmethod
    def execute(self, game: "Game") -> None:
        """
        Выполняет что-то, если в меню была выбрана эта категория.
        :param game: Экземпляр класса Game.
        :return: None
        """

    @property
    def name(self) -> str:
        """
        Возвращает название категории.
        :return: Название категории (str).
        """
        return self._name
