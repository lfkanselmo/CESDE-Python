class service:
    description = None
    base_fee = None
    def __init__(self, description, base_fee):
        self._description = description
        self._base_fee = base_fee


    def calculate_fee(self):
        return self._base_fee

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def base_fee(self):
        return self._base_fee

    @base_fee.setter
    def base_fee(self, base_fee):
        self._base_fee = base_fee