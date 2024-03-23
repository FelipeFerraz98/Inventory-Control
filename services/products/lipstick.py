from .controlers.productcontroller import *

class Lipstick(ProductController):
    def __init__(self) -> None:
        super().__init__('unisex', 'batom')