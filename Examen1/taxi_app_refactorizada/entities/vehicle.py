class vehicle:

    make = None
    model = None
    year = None
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def __str__(self):
        return f"Marca: {self._make}   Modelo: {self._model}     Año: {self._year}"

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year
