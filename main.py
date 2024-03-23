from services.products.shampoo import *


shampoo_masculine = MenShampoo()
shampoo_masculine.decrease_quantity('liso', 100)
shampoo_masculine.add_product('bra', 2, 100.00)
shampoo_masculine.edit_price('bra', 0)
