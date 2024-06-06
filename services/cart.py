class Cart:
    """
    Classe Cart para gerenciar o carrinho de compras.
    
    Atributos:
    - items (list): Lista de dicionários contendo produtos, suas quantidades e preços.
    
    Métodos:
    - add_item(self, product, genere, quantity, price): Adiciona um item ao carrinho.
    - display_cart(self): Exibe o conteúdo do carrinho.
    - get_total(self): Calcula o total do carrinho.
    - checkout(self): Processa a finalização da compra, atualizando o estoque.
    """
    
    def __init__(self):
        self.items = []
    
    def add_item(self, product, genere, quantity, price):
        """
        Adiciona um item ao carrinho.
        
        Parâmetros:
        - product (str): O nome do produto.
        - genere (str): O gênero do produto.
        - quantity (int): A quantidade do produto.
        - price (float): O preço do produto.
        """
        self.items.append({
            'product': product,
            'genere': genere,
            'quantity': quantity,
            'price': price
        })
    
    def display_cart(self):
        """
        Exibe o conteúdo do carrinho.
        
        Retorna:
        - None
        """
        if not self.items:
            print("O carrinho está vazio.")
            return
        
        print("Produtos no carrinho:")
        for item in self.items:
            print(f"{item['product']} - {item['genere']} - Quantidade: {item['quantity']} - Preço: {item['price']} - Total: {item['quantity'] * item['price']}")
    
    def get_total(self):
        """
        Calcula o total do carrinho.
        
        Retorna:
        - float: O total do carrinho.
        """
        total = sum(item['quantity'] * item['price'] for item in self.items)
        return total
    
    def checkout(self, screen_instance):
        """
        Processa a finalização da compra, atualizando o estoque.
        
        Parâmetros:
        - screen_instance (Screen): Instância da classe Screen para acessar os métodos de atualização de estoque.
        
        Retorna:
        - None
        """
        self.display_cart()
        total = self.get_total()
        print(f"Total a pagar: {total}")
        
        confirmation = input("Deseja confirmar a compra? (s/n): ")
        if confirmation.lower() == 's':
            for item in self.items:
                screen_instance._save_product(item['genere']).decrease_quantity(item['product'], item['quantity'])
            print("Compra confirmada! Estoque atualizado.")
        else:
            print("Compra cancelada.")
        
        # Limpa o carrinho após a compra ou cancelamento
        self.items.clear()
