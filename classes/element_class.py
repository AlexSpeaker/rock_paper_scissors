from typing import Optional


class Element:
    _resist: Optional["Element"] = None

    def __init__(self, element_name: str):
        self._element_name = element_name

    @property
    def element_name(self) -> str:
        return self._element_name

    @property
    def resist(self) -> Optional["Element"]:
        return self._resist

    @resist.setter
    def resist(self, resist_element: "Element"):
        self._resist = resist_element
