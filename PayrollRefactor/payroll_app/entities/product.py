from payroll_app.entities.category import category


class product:
    id = None
    name = None
    price = None
    quantity = None
    description = None
    product_category = None
    _products = {}

    def __init__(self, id, name, price, quantity, description, product_category):
        self._id = id
        self._name = name
        self._price = price
        self._quantity = quantity
        self._description = description
        self._product_category = product_category


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def product_category(self):
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        self._product_category = product_category

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products

    def create_product(self):
        self._id = input("Insert product ID: ")
        self._name = input("Insert product name: ")
        self._price = int(input("Insert product price: "))
        self._quantity = int(input("Insert product quantity: "))
        self._description = input("Insert product description: ")
        self._product_category = category.search_category()

        self._products[self._id] = {"Name": self._name, "Price": self._price, "Quantity": self._quantity,"Description": self._description, "Category": self._product_category}


    def print_product(self):
        print( f"""
            Name: {self._name}
            Category: {self._product_category["Name"]}
            """)