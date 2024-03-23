from .controler import *
from .exceptions import *

class ProductControler(Data):
    def __init__(self) -> None:
        super().__init__()

    def declare_variable(self, gender, product):
        self._gender = gender
        self._product = product

    def add_product(self, product) -> None:
        data = self.load_json()
        data[product] = {}
        self.save_json(data)

    def increase_quantity(self, type, quantity_increase) -> None:
        data = self.load_json()
        if self._product in data and self._gender in data[self._product] and type in data[self._product][self._gender]:
            data[self._product][self._gender][type]['quantidade'] += quantity_increase
            self.save_json(data)
            print(f"The quantity of type {type} {self._gender} has been increased by {quantity_increase}.")
        else:
            raise InvalidProduct("Produto não encontrado!")

    def decrease_quantity(self, type, quantity_decrease) -> None:
        data = self.load_json()
        if self._product in data and self._gender in data[self._product] and type in data[self._product][self._gender]:
            current_quantity = data[self._product][self._gender][type]['quantidade']
            if quantity_decrease <= current_quantity:
                if quantity_decrease >= current_quantity:
                    data[self._product][self._gender][type]['quantidade'] = 0
                    self.save_json(data)
                    print(f"The entire stock of type {type} {self._gender} has been depleted. Quantity removed: {current_quantity}.")
                else:
                    data[self._product][self._gender][type]['quantidade'] -= quantity_decrease
                    self.save_json(data)
                    print(f"The quantity of type {type} {self._gender} has been decreased by {quantity_decrease}.")
        else:
            raise InvalidProduct("Produto não encontrado!")

    def add_type_product(self, type, quantity) -> None:
        data = self.load_json()
        if self._product in data and self._gender in data[self._product]:
            if type not in data[self._product][self._gender]:
                data[self._product][self._gender][type] = {'quantidade': quantity}
                self.save_json(data)
                print(f"New product of type {type} {self._gender} has been added.")
        else:
            raise InvalidProduct("Produto não encontrado!")

    def check_zero_quantity(self) -> None:
        data = self.load_json()
        zero_products = []
        if self._product in data and self._gender in data[self._product]:
            for product_type, product_info in data[self._product][self._gender].items():
                if product_info['quantidade'] == 0:
                    zero_products.append(product_type)
        return zero_products