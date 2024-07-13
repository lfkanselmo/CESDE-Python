from connection import connection

db = connection(host = 'localhost', port = 3306, user = 'root', password = '', database = 'tienda')
db.connect()