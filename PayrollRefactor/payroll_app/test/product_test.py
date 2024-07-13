from payroll_app.entities.category import category
from payroll_app.entities.product import product

category = category(None,None)
category.create_category()
category.create_category()

product = product(None, None, None, None,None,None)

for item in category.categories.values():
    print(item)

product.create_product()

for item in product.products.values():
    print(item)