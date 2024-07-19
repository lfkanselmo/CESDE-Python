class product_sale:
    id_sale = None
    costumer = None
    employee = None
    product = None
    quantity = None
    total = None
    def __init__(self, id_sale, costumer, employee, product, quantity):
        self._id_sale = id_sale
        self._costumer = costumer
        self._employee = employee
        self._product = product
        self._quantity = quantity
        self._total = self.calculate_total()

    @property
    def id_sale(self):
        return self._id_sale

    @id_sale.setter
    def id_sale(self, id_sale):
        self._id_sale = id_sale

    @property
    def costumer(self):
        return self._costumer

    @costumer.setter
    def costumer(self, costumer):
        self._costumer = costumer

    @property
    def employee(self):
        return self._employee

    @employee.setter
    def employee(self, employee):
        self._employee = employee

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    def calculate_total(self):
        return self.quantity * self.product.price
