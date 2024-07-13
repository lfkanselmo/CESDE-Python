import mysql.connector
class connection:

    _instance = None
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print("Database connection success")
        except mysql.connector.Error as err:
            print("Database connection failed")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query, params = None):
        cursor = self.connection.cursor(buffered = True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Query execute success")
            if query.lower().startswith("select"):
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print("Query execute failed")
            return None
        finally:
            cursor.close()

    @staticmethod
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(connection, cls).__new__(cls)
            try:
