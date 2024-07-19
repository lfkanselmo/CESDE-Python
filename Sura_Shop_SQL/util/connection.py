import mysql.connector
from mysql.connector import Error
class connection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(connection, cls).__new__(cls)
        return cls._instance

    def __init__(self, host, port, database, user, password):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self._initialized = True

    def connect(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    port=self.port,
                    database=self.database,
                    user=self.user,
                    password=self.password
                )
                if self.connection.is_connected():
                    print("database connection success")
            except Error as e:
                print(f"connection failed: {e}")
                self.connection = None


    def get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            self.connect()
        return self.connection

    def close_connection(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Connection closed")
            self.connection = None

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

