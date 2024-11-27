from core.classes.element import Element

stone = Element("Камень")
scissors = Element("Ножницы")
paper = Element("Бумага")

stone.resists_element = scissors
scissors.resists_element = paper
paper.resists_element = stone
