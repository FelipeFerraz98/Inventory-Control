'''Criação de erros personalizados'''

class InvalidProduct(Exception):
    pass

class ExistingProduct(Exception):
    pass

class InvalidPrice(Exception):
    pass