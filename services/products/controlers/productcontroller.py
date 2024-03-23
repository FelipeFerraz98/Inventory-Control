from .controller import *
from .exceptions import *

class ProductController(Data):
    def __init__(self, gender, product) -> None:
        super().__init__()
        self._gender = gender
        self._product = product    

    def increase_quantity(self, type, quantity_increase) -> bool:
        data = self.load_json()
        try:
            data[self._product][self._gender][type]['quantidade'] += quantity_increase
            self.save_json(data)
            return True
        except:
            raise InvalidProduct("Produto não encontrado!")

    def decrease_quantity(self, type, quantity_decrease) -> bool:
        data = self.load_json()
        try:
            current_quantity = data[self._product][self._gender][type]['quantidade']
            if quantity_decrease <= current_quantity:
                if quantity_decrease >= current_quantity:
                    data[self._product][self._gender][type]['quantidade'] = 0
                    self.save_json(data)
                    return True
                else:
                    data[self._product][self._gender][type]['quantidade'] -= quantity_decrease
                    self.save_json(data)
                    return True
        except:
            raise InvalidProduct("Produto não encontrado!")

    def add_type_product(self, type, quantity) -> bool:
        data = self.load_json()
        try:
            if type not in data[self._product][self._gender]:
                data[self._product][self._gender][type] = {'quantidade': quantity}
                self.save_json(data)
            else:
                raise ExistingProduct ("Já existe este produto, tente adicionar quantidade ao estoque!")
        except:
            raise InvalidProduct("Produto não encontrado!")

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