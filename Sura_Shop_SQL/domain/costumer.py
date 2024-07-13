from domain.user import user
from util.connection import connection

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

    def costumer_insert(self,db):
        query = f"INSERT INTO costumer (costumer_id, costumer_name, costumer_last_name, costumer_email, costumer_password, costumer_type, points) VALUES({self.id}, {self.name}, {self.last_name}, {self.email}, {self.password}, {self.type}, {self.points})"
        connection.get_connection()