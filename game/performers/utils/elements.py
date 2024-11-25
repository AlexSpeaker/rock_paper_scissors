from classes.element.element import Element

"""
Создаём элементы для игры.
"""

paper = Element("Бумага")
stone = Element("Камень")
scissors = Element("Ножницы")
paper.resists_the_element = stone
stone.resists_the_element = scissors
scissors.resists_the_element = paper
