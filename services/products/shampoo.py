from .controlers.productcontroller import *

class MenShampoo(ProductController):
    def __init__(self) -> None:
        super().__init__('masculino', 'shampoo')

class WomenShampoo(ProductController):
    def __init__(self) -> None:
        super().__init__('feminino', 'shampoo')