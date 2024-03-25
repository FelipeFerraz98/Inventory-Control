from services.products import shampoo, lipstick, perfume
from screenexceptions import *

class Screen():
    def __init__(self) -> None:
        self._shampoo = shampoo.Shampoo
        self._perfume = perfume.Perfume
        self._lipstick = lipstick.Lipstick

        self._initial_choice : int
        self._product_choice : int
        self._genere_choice : int

        self._choice_actions = {
            0: self._handle_unisex,
            1: self._handle_male,
            2: self._handle_female,
            3: self._handle_child
        }

    def _product_menu(self) -> None:
        while True:
            try:
                print("""Selecione uma das opções
                    1 - Shampoo
                    2 - Perfume
                    3 - Batom
                    """)
                product_choice = int(input("Digite aqui sua opção: "))

                if product_choice not in [1,2,3]: # array com opções válidas
                    raise InvalidChoice("Opção inválida! Tente novamente!")

                self._genere_menu(product_choice)

                return
            except(InvalidChoice, ValueError):
                raise InvalidChoice("Opção inválida! Tente novamente!")
            
    def _genere_menu(self, product: int) -> None:
        while True:
            try:
                if product == 1:
                    print("""Selecione uma das opções
                        1 - Masculino
                        2 - Feminino
                        """)
                    self._save_product = self._shampoo
                    genere_choice = int(input("Digite aqui sua opção: "))
                    if genere_choice not in [1,2]: # array com opções válidas
                        raise InvalidChoice("Opção inválida! Tente novamente!")

                elif product == 2:
                    print("""Selecione uma das opções
                        1 - Masculino
                        2 - Feminino
                        3 - Infantil
                        """)
                    self._save_product = self._perfume
                    genere_choice = int(input("Digite aqui sua opção: "))
                    if genere_choice not in [1,2,3]: # array com opções válidas
                        raise InvalidChoice("Opção inválida! Tente novamente!")
                    
                elif product == 3:
                    self._handle_choice(0)
                    self._save_product = self._lipstick

                self._handle_choice(genere_choice)

                return

            except(InvalidChoice, ValueError):
                raise InvalidChoice("Opção inválida! Tente novamente!")
    
    def _print_products(self, genere: str) -> list:
        action = self._shampoo(genere)
        list_products = action.all_products()
        index = 0
        print("Escolha um produto:")
        for product in list_products:
            index += 1
            print(f"{index} - {product}")
        try:    
            choice = int(input("Digite uma opção: "))
            if choice <= index and choice > 0:
                return list_products, choice - 1 # retornando a lista e a escolha -1 (array comeca em 0)
            raise InvalidChoice("Opção inválida!")
        except(InvalidChoice, ValueError):
            raise InvalidChoice("Opção inválida!")
        
    def _print_products_details(self, genere: str) -> list:
        action = self._shampoo(genere)
        list_products = action.all_products_details()
        return list_products

    def _increase_product(self, genere: str):
        action = self._save_product(genere)
        products, choice = self._print_products(genere)
        products_details = self._print_products_details(genere)
        print(f"Detalhes do produto {products[choice]}")
        print(products_details[choice])
        while True:
            try:
                add_quantity = int(input("Digite a quantidade que deseja adicionar: "))
                validate = action.increase_quantity(products[choice], add_quantity)
                if validate:
                    print("Quantidade adicionada!")
                    products_details = self._print_products_details(genere)
                    print(f"Novo total: {products_details[choice]}")
                    return
            except:
                raise ValueError("Valor inválido, digite um valor válido!")

    def _decrease_stock(self, genere) -> None:
        action = self._save_product(genere)
        products, choice = self._print_products(genere)
        products_details = self._print_products_details(genere)
        print(f"Detalhes do produto {products[choice]}")
        print(products_details[choice])
        while True:
            try:
                decrease_quantity = int(input("Digite a quantidade que deseja retirar: "))
                validate = action.increase_quantity(products[choice], decrease_quantity)
                if validate:
                    print("Quantidade retirada!")
                    products_details = self._print_products_details(genere)
                    print(f"Novo total: {products_details[choice]}")
                    return
            except:
                raise ValueError("Valor inválido, digite um valor válido!")
    
    def _create_product(self, genere: str) -> None:
        action = self._save_product(genere)
        while True:
            try:
                product = input("Digite o produto: ")
                quantity = int(input("Digite a quantidade: "))
                price = float(input("Digite o preço: "))
                validate = action.add_product(product, quantity, price)
                if validate:
                    print("Produto adicionado!")
                    products = self._print_products_details(genere)
                    print(f"Novo produto: {products[-1]}")
                    return
            except:
                raise ValueError("Valor inválido, digite um valor válido!")

    def _change_product_price(self, genere: str) -> None:
        action = self._save_product(genere)
        action.edit_price()
        products, choice = self._print_products(genere)
        products_details = self._print_products_details(genere)
        print(f"Detalhes do produto {products[choice]}")
        print(products_details[choice])
        while True:
            try:
                price = int(input("Digite o novo preço do produto: "))
                validate = action.edit_price(products[choice], price)
                if validate:
                    print("Preço alterado!")
                    products_details = self._print_products_details(genere)
                    print(f"Novo preço: {products_details[choice]}")
                    return
            except:
                raise ValueError("Valor inválido, digite um valor válido!")

    def _handle_crud(self, genere: str) -> None:
        if self._initial_choice == 1: 
            self._increase_product(genere)
        elif self._initial_choice == 2: 
            self._create_product(genere)
        elif self._initial_choice == 3: 
            self._change_product_price(genere)
        elif self._initial_choice == 4: 
            self._decrease_stock(genere)
    
    def _handle_unisex(self) -> None:
        self._handle_crud('unisex')

    def _handle_male(self) -> None:
        self._handle_crud('masculino')  

    def _handle_female(self) -> None:
        self._handle_crud('feminino')  

    def _handle_child(self) -> None:
        self._handle_crud('infantil')  


    def _handle_choice(self, genere : int) -> None:
        action = self._choice_actions.get(genere) # reduzindo uso de if's usando dicionário
        action() # executando o método salvo em self._choice_actions

    def initial_menu(self) -> None:
        while True:
            try:
                print("""Selecione uma das opções
                    1 - adicionar produto já existente ao estoque
                    2 - adicionar um novo produto ao estoque
                    3 - alterar preço de um produto ao estoque
                    4 - vender um produto
                    """)
                self._initial_choice = int(input("Digite aqui sua opção: "))
                if self._initial_choice not in [1,2,3,4]: # array com opções válidas
                    raise InvalidChoice("Opção inválida! Tente novamente!")
                
                self._product_menu()

                return
            except(InvalidChoice, ValueError):
                raise InvalidChoice("Opção inválida! Tente novamente!")
            