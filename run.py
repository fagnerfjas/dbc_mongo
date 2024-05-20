from models.connections.mongo_connect import DbConnectionManager 

db_adm = DbConnectionManager()

connection1 = db_adm.get_db_connection()
print(connection1)

db_adm.connect_to_db()
connection2 = db_adm.get_db_connection()
print(connection2)
