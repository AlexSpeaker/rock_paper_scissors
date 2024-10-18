import random
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

from classes.element_class import Element
from classes.exception_class import EndGame, NoElementResist
from classes.player_class import Player


class GameMenu(ABC):
    _main_menu_list = ["Начать игру.", "Статистика.", "Выход."]
    _errors_list = [
        "Ошибка ввода! Вводить нужно только цифры и цифры должны быть положительными!",
        "Ошибка ввода! Вне диапазона меню!",
    ]

    def _menu_validator(
        self, choice: str, menu_list: List[Any]
    ) -> Dict[str, Union[str, bool, None]]:
        if not choice.isdigit():
            return {"result": False, "message": self._errors_list[0]}
        elif int(choice) > len(menu_list) or int(choice) < 1:
            return {"result": False, "message": self._errors_list[1]}
        return {"result": True, "message": None}

    def _menu(self):
        while True:
            print("Меню:")
            print(
                "\n".join(
                    [f"\t{i}. {name}" for i, name in enumerate(self._main_menu_list, 1)]
                )
            )
            choice = input("Сделайте Ваш выбор: ").strip()
            validate_menu = self._menu_validator(choice, self._main_menu_list)
            if validate_menu["result"]:
                break
            else:
                print(validate_menu["message"])
        match choice:
            case "1":
                self._start_game()
            case "2":
                self._game_statistics()
            case "3":
                raise EndGame

    def _elements_menu(self, elements_list: List[Element]) -> Element:
        while True:
            print("Выберите элемент:")
            print(
                "\n".join(
                    [
                        f"\t{i}. {element.element_name}"
                        for i, element in enumerate(elements_list, 1)
                    ]
                )
            )
            element_num = input("Сделайте Ваш выбор: ").strip()
            validate_menu = self._menu_validator(element_num, elements_list)
            if validate_menu["result"]:
                break
            else:
                print(validate_menu["message"])
        return elements_list[int(element_num) - 1]

    @abstractmethod
    def _start_game(self):
        pass

    @abstractmethod
    def _game_statistics(self):
        pass


class Game(GameMenu):
    def __init__(
        self,
        player_1: Player,
        player_2: Player,
        list_elements: Optional[List[Element]] = None,
    ):
        self._player_1 = player_1
        self._player_2 = player_2
        self._players = [self._player_1, self._player_2]

        self._list_elements = (
            self._get_elements() if list_elements is None else list_elements
        )
        self._elements_validator(self._list_elements)

    @staticmethod
    def _elements_validator(elements_list: List[Element]):
        for element in elements_list:
            if not isinstance(element.resist, Element):
                raise NoElementResist(element.element_name)

    @staticmethod
    def _get_elements() -> List[Element]:
        stone = Element("Камень")
        scissors = Element("Ножницы")
        paper = Element("Бумага")

        stone.resist = scissors
        scissors.resist = paper
        paper.resist = stone

        return [stone, scissors, paper]

    def _determine_the_winner(self):
        if self._player_1.my_element == self._player_2.my_element:
            print("*" * 100)
            print("Ничья!")
            print("*" * 100)
            return
        elif self._player_1.my_element.resist == self._player_2.my_element:
            winner_player = self._player_1
            loser_player = self._player_2
        else:
            winner_player = self._player_2
            loser_player = self._player_1
        print("*" * 100)
        print(f"Игрок {winner_player.name} победил!!!")
        print(
            f"Игрок {winner_player.name} выбрал {winner_player.my_element.element_name}"
        )
        print(
            f"Игрок {loser_player.name} выбрал {loser_player.my_element.element_name}"
        )
        print("*" * 100)
        winner_player.add_wins()
        loser_player.add_losses()

    def _start_game(self):
        for player in self._players:
            if not player.computer:
                print(f"Игрок {player.name}:")
                element = self._elements_menu(self._list_elements)
            else:
                element = random.choice(self._list_elements)
            player.my_element = element
        self._determine_the_winner()

    def _game_statistics(self):
        print("-" * 100)
        for player in self._players:
            print(f"Игрок: {player.name}")
            print(f"\tПобед: {player.wins}")
            print(f"\tПоражений: {player.losses}")
            print("-" * 100)

    def game_run(self):
        while True:
            try:
                self._menu()
            except EndGame:
                exit(0)
