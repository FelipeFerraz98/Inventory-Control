from .controlers.productcontroler import *

class ShampooMasculine(ProductControler):
    def __init__(self) -> None:
        super().__init__()
        super().declare_variable('masculino', 'shampoo')

class ShampooFeminine(ProductControler):
    def __init__(self) -> None:
        super().__init__()
        super().declare_variable('feminino', 'shampoo')
