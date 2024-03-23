from services.products import shampoo, lipstick, perfume
from screenexceptions import *

class Screen():
    def __init__(self) -> None:
        self._men_shampoo = shampoo.MenShampoo()
        self._women_shampoo = shampoo.WomenShampoo()

        self._men_perfume = perfume.MenPerfume()
        self._women_perfume = perfume.WomenPerfume()
        self._children_perfume = perfume.ChildrenPerfume()

        self._lipstick = lipstick.Lipstick()

    def menu(self) -> None:
        while True:
            try:
                print("""Selecione uma das opções
                    1 - adicionar produto já existente ao estoque
                    2 - adicionar um novo produto ao estoque
                    3 - alterar preço de um produto ao estoque
                    4 - vender um produto
                    """)
                choice = int(input("Digite aqui sua opção: "))
                self.choices(choice)
            except(InvalidChoice):
                raise InvalidChoice("Opção inválida! Tente novamente!")
    
    def choices(self, choice: int):


    def print_screen(self) -> None:
        self.menu()