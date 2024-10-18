from typing import Optional

from classes.element_class import Element


class Player:
    _number_of_wins: int = 0
    _number_of_losses: int = 0
    _my_element: Optional[Element] = None

    def __init__(self, player_name: str, computer: bool = False):
        self._player_name = player_name
        self._computer = computer

    @property
    def wins(self) -> int:
        return self._number_of_wins

    @property
    def losses(self) -> int:
        return self._number_of_losses

    @property
    def name(self) -> str:
        return self._player_name

    def add_wins(self):
        self._number_of_wins += 1

    def add_losses(self):
        self._number_of_losses += 1

    @property
    def my_element(self) -> Optional[Element]:
        return self._my_element

    @my_element.setter
    def my_element(self, element: Element):
        self._my_element = element

    @property
    def computer(self) -> bool:
        return self._computer
