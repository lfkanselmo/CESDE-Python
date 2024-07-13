from payroll_app.entities.user import user


class costumer(user):
    type = None
    points = None

    def __init__(self, id, name, last_name, email, password, type, points):
        super().__init__(id, name, last_name, email, password)
        self._type = type
        self._points = points

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def points(self):
        return  self._points

    @points.setter
    def points(self, points):
        self._points = points



    def create_costumer(self):
        super().create()
        self._type = input("Insert type: ")
        self._type = 0

        costumer_saved = {}

        costumer_saved[self._id] = {"name": self._name, "last_name": self._last_name,
                    "email": self._email, "password": self._password, "points": self._points,
                    "type": self._type}

        self.save(costumer_saved)