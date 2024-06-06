from services.products import shampoo, lipstick, perfume
from screenexceptions import *
import time

class Screen():
    def __init__(self) -> None:
        # Inicializa as classes de produtos
        self._shampoo = shampoo.Shampoo
        self._perfume = perfume.Perfume
        self._lipstick = lipstick.Lipstick

        # Inicializa variáveis de escolha
        self._initial_choice : int
        self._product_choice : int
        self._genere_choice : int

        # Dicionário que mapeia escolhas para os métodos correspondentes
        self._choice_actions = {
            0: self._handle_unisex,
            1: self._handle_male,
            2: self._handle_female,
            3: self._handle_child
        }

    # Método para exibir o menu de produtos e capturar a escolha do usuário
    def _product_menu(self) -> None:
        """
        Exibe o menu de seleção de produtos e gerencia a escolha do usuário.
        """

        while True:
            try:
                print("""Selecione uma das opções
                    1 - Shampoo
                    2 - Perfume
                    3 - Batom
                    """)
                product_choice = int(input("Digite aqui sua opção: "))

                # Verifica se a escolha é válida
                if product_choice not in [1, 2, 3]:
                    raise InvalidChoice("Opção inválida! Tente novamente!")

                # Chama o menu de gênero com base na escolha do produto
                self._genere_menu(product_choice)

                return
            except (InvalidChoice, ValueError):
                raise InvalidChoice("Opção inválida! Tente novamente!")

    # Método para exibir o menu de gêneros e capturar a escolha do usuário
    def _genere_menu(self, product: int) -> None:
        """
        Exibe o menu de seleção de gênero do produto e gerencia a escolha do usuário.
        
        Parâmetros:
        - product: O tipo de produto escolhido pelo usuário.
        """

        while True:
            try:
                if product == 1:
                    print("""Selecione uma das opções
                        1 - Masculino
                        2 - Feminino
                        """)
                    self._save_product = self._shampoo
                    genere_choice = int(input("Digite aqui sua opção: "))
                    if genere_choice not in [1, 2]:
                        raise InvalidChoice("Opção inválida! Tente novamente!")

                elif product == 2:
                    print("""Selecione uma das opções
                        1 - Masculino
                        2 - Feminino
                        3 - Infantil
                        """)
                    self._save_product = self._perfume
                    genere_choice = int(input("Digite aqui sua opção: "))
                    if genere_choice not in [1, 2, 3]:
                        raise InvalidChoice("Opção inválida! Tente novamente!")

                elif product == 3:
                    self._handle_choice(0)  # Batom é unissex
                    self._save_product = self._lipstick

                # Processa a escolha do gênero
                self._handle_choice(genere_choice)

                return
            except (InvalidChoice, ValueError):
                raise InvalidChoice("Opção inválida! Tente novamente!")

    # Método para exibir os produtos e capturar a escolha do usuário
    def _print_products(self, genere: str) -> list:
        """
        Exibe a lista de produtos de um gênero específico e coleta a escolha do usuário.
        
        Parâmetros:
        - genere: O gênero dos produtos a serem exibidos.
        
        Retorna:
        - Uma lista com os produtos disponíveis e a escolha do usuário.
        
        Lança:
        - InvalidChoice se a escolha for inválida.
        """
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
                return list_products, choice - 1  # retornando a lista e a escolha -1 (array comeca em 0)
            raise InvalidChoice("Opção inválida!")
        except (InvalidChoice, ValueError):
            raise InvalidChoice("Opção inválida!")

    # Método para exibir os detalhes dos produtos
    def _print_products_details(self, genere: str) -> list:
        """
        Exibe detalhes de todos os produtos de um gênero específico.
        
        Parâmetros:
        - genere: O gênero dos produtos.
        
        Retorna:
        - Uma lista com detalhes dos produtos.
        """

        action = self._shampoo(genere)
        list_products = action.all_products_details()
        return list_products

    # Método para aumentar a quantidade de um produto no estoque
    def _increase_product(self, genere: str):
        """
        Aumenta a quantidade de um produto.
        
        Parâmetros:
        - genere: O gênero do produto.
        """
        
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

    # Método para diminuir a quantidade de um produto no estoque (venda)
    def _decrease_stock(self, genere) -> None:
        """
        Diminui a quantidade de um produto.
        
        Parâmetros:
        - genere: O gênero do produto.
        """

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

    # Método para criar um novo produto
    def _create_product(self, genere: str) -> None:
        """
        Adiciona um novo produto.
        
        Parâmetros:
        - genere: O gênero do produto.
        """

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

    # Método para alterar o preço de um produto
    def _change_product_price(self, genere: str) -> None:
        """
        Altera o preço de um produto.
        
        Parâmetros:
        - genere: O gênero do produto.
        """

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

    # Método para lidar com operações CRUD com base na escolha inicial
    def _handle_crud(self, genere: str) -> None:
        """
        Gerencia operações de CRUD com base na escolha inicial do usuário.
        
        Parâmetros:
        - genere: O gênero do produto.
        """
        if self._initial_choice == 1: 
            self._increase_product(genere)
        elif self._initial_choice == 2: 
            self._create_product(genere)
        elif self._initial_choice == 3: 
            self._change_product_price(genere)
        elif self._initial_choice == 4: 
            self._decrease_stock(genere)

    # Métodos para lidar com cada tipo de produto com base no gênero
    def _handle_unisex(self) -> None:
        """
        Lida com operações em produtos unissex.
        """
        self._handle_crud('unisex')

    def _handle_male(self) -> None:
        """
        Lida com operações em produtos masculinos.
        """
        self._handle_crud('masculino')  

    def _handle_female(self) -> None:
        """
        Lida com operações em produtos femininos.
        """
        self._handle_crud('feminino')  

    def _handle_child(self) -> None:
        """
        Lida com operações em produtos infantis.
        """ 
        self._handle_crud('infantil')  

    # Método para lidar com a escolha de gênero usando o dicionário
    def _handle_choice(self, genere : int) -> None:
        """
        Chama a função apropriada com base na escolha do usuário.
        
        Parâmetros:
        - genere: A escolha do gênero feita pelo usuário.
        """
        action = self._choice_actions.get(genere)
        action()  # Executa o método correspondente à escolha do gênero

    # Método para verificar produtos com quantidade zero
    def _check_zero_products(self) -> list:
        """
        Verifica quais produtos estão com quantidade zero.
        
        Retorna:
        - Uma lista de produtos com quantidade zero.
        """
        generes = ['unisex', 'masculino', 'feminino', 'infantil']
        validates = []

        # Verifica shampoo em falta
        shampoo_zero = self._shampoo(generes[1]).check_zero_quantity()
        if shampoo_zero:
            validates.append(f'Shampoo {generes[1]} em falta:')
            validates.append(shampoo_zero)

        shampoo_zero = self._shampoo(generes[2]).check_zero_quantity()
        if shampoo_zero:
            validates.append(f'Shampoo {generes[2]} em falta:')
            validates.append(shampoo_zero)

        # Verifica batom em falta
        lipstick_zero = self._lipstick(generes[0]).check_zero_quantity()
        if lipstick_zero:
            validates.append('Batom em falta:')
            validates.append(lipstick_zero)

        # Verifica perfume em falta
        perfume_zero = self._perfume(generes[1]).check_zero_quantity()
        if perfume_zero:
            validates.append(f'Perfume {generes[1]} em falta:')
            validates.append(perfume_zero)

        perfume_zero = self._perfume(generes[2]).check_zero_quantity()
        if perfume_zero:
            validates.append(f'Perfume {generes[2]} em falta:')
            validates.append(perfume_zero)

        perfume_zero = self._perfume(generes[3]).check_zero_quantity()
        if perfume_zero:
            validates.append(f'Perfume {generes[3]} em falta:')
            validates.append(perfume_zero)

        return validates

    # Método inicial para exibir o menu principal e capturar a escolha do usuário
    def initial_menu(self) -> None:
        """
        Exibe o menu inicial e gerencia a escolha do usuário.
        """
        
        while True:
            validates = self._check_zero_products()
            if validates:
                for zero_products in validates:
                    print(zero_products)
                    time.sleep(1)
            try:
                print("""Selecione uma das opções
                    1 - adicionar produto já existente ao estoque
                    2 - adicionar um novo produto ao estoque
                    3 - alterar preço de um produto ao estoque
                    4 - vender um produto
                    """)
                self._initial_choice = int(input("Digite aqui sua opção: "))
                if self._initial_choice not in [1, 2, 3, 4]:
                    raise InvalidChoice("Opção inválida! Tente novamente!")

                self._product_menu()

                return
            except (InvalidChoice, ValueError):
                raise InvalidChoice("Opção inválida! Tente novamente!")
