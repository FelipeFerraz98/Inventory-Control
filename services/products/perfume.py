from .controlers.productcontroller import *

class MenPerfume(ProductController):
    def __init__(self) -> None:
        super().__init__('masculino', 'perfume')

class WomenPerfume(ProductController):
    def __init__(self) -> None:
        super().__init__('feminino', 'perfume')

class ChildrenPerfume(ProductController):
    def __init__(self) -> None:
        super().__init__('infantil', 'perfume')