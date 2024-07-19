from connection import connection
db = connection(host = 'localhost', port = 3306, database = 'tienda', user = 'root' , password = '1152')
db.connect()