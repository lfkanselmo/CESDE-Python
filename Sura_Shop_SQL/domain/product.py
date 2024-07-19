class product:
    id = None
    name = None
    price = None
    quantity = None
    description = None
    product_category = None

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
