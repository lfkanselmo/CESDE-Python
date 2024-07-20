from domain.user import user
from util.connection import connection

class costumer(user):
    type = None
    points = None
    db = connection()

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

    def create(self):
        super().create()
        self._type = input("Insert type: ")
        self._points = int(input("Insert point: "))

    def costumer_insert(self,db):
        query = f"INSERT INTO costumer (%d, %s, %s, %s, %s, %d, %d)"
        values = (self.id, self.name, self.last_name, self.email, self.password, self.type, self.points)
        self.db.connect()
        self.db.execute_query(query, values)
        self.db.close_connection()