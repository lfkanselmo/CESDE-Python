from util.connection import connection
class costumer_type:
    db = connection()
    def __init__(self, type):
        self._type = type

    @property
    def type(self):
        return self._type

    def type(self, type):
        self._type = type

    def create(self):
        query = "INSERT INTO costumer_type(costumer_type) VALUES(%s)"
        values = (self._type,)
        self.db.connect()
        if self.search_type():
            print(f"Already exist. Not possible save costumer type {self._type}")
        else:
            self.db.execute_query(query, values)
        self.db.close_connection()

    def search_type(self):
        type = input("Insert type to select: ")
        query = "SELECT * FROM costumer_type WHERE %s = costumer_type"
        values = (type,)
        self.db.connect()
        type_searched = self.db.execute_query(query, values)
        self.db.close_connection()
        return type_searched
