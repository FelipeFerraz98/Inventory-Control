from services.products.shampoo import *


shampoo_masculine = ShampooMasculine()
shampoo_masculine.add_type_product('grisalio', 10)
shampoo_masculine.increase_quantity('grisalio', 5)
shampoo_masculine.decrease_quantity('grisalio', 2)
shampoo_masculine.decrease_quantity('grisalio', 2)
ProductControler().add_product('leve')