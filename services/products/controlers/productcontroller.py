from .controller import *
from .productsexceptions import *

class ProductController(Data):
    def __init__(self, gender, product) -> None:
        super().__init__()
        self._gender = gender
        self._product = product    

    def edit_price(self, type : str, price: float) -> bool:
        data = self.load_json()
        try:
            if price > 0:
                data[self._product][self._gender][type]['preco'] = price
                self.save_json(data)
                return True
            else:
                raise InvalidPrice("O preço não pode ser 0 ou menor!")
        except(InvalidProduct):
            raise InvalidProduct("Produto não encontrado!")

    def increase_quantity(self, type: str, quantity_increase: int) -> bool:
        data = self.load_json()
        try:
            data[self._product][self._gender][type]['quantidade'] += quantity_increase
            self.save_json(data)
            return True
        except(InvalidProduct):
            raise InvalidProduct("Produto não encontrado!")

    def decrease_quantity(self, type: str, quantity_decrease: int) -> bool:
        data = self.load_json()
        try:
            current_quantity = data[self._product][self._gender][type]['quantidade']
            if quantity_decrease >= current_quantity:
                data[self._product][self._gender][type]['quantidade'] = 0
                self.save_json(data)
                return True
            else:
                data[self._product][self._gender][type]['quantidade'] -= quantity_decrease
                self.save_json(data)
                return True
        except(InvalidProduct):
            raise InvalidProduct("Produto não encontrado!")

    def add_product(self, type: str, quantity: int, price: float) -> bool:
        data = self.load_json()
        try:
            if type not in data[self._product][self._gender]:
                data[self._product][self._gender][type] = {'quantidade': quantity, 'preco': price}
                self.save_json(data)
            else:
                raise ExistingProduct ("Já existe este produto, tente adicionar quantidade ao estoque!")
        except(InvalidProduct):
            raise InvalidProduct("Produto inválido!")

    def check_zero_quantity(self) -> bool:
        data = self.load_json()
        zero_products = []
        try:
            for product_type, product_info in data[self._product][self._gender].items():
                if product_info['quantidade'] == 0:
                    zero_products.append(product_type)
            return zero_products
        except:
            raise InvalidProduct("Produto não encontrado!")
        
    def all_products(self) -> list:
        data = self.load_json()
        products = []
        for product_type in data[self._product][self._gender]:
            products.append(product_type)
        return products
    
    def all_products_details(self) -> list:
        data = self.load_json()
        products = []
        for product_type in data[self._product][self._gender].items():
            products.append(product_type)
        return products