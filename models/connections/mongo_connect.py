from pymongo import MongoClient
from config import mongo_config


'''
    Object to manage mongodb connection
'''
class DbConnectionManager:
    def __init__(self) -> None:
        self.__connection_string = 'mongodb://{}:{}@{}:{}'.format(
            mongo_config['USER'],
            mongo_config['PASS'],
            mongo_config['HOST'], 
            mongo_config['PORT']
        )
        self.__db_name = mongo_config['DB_NAME']
        self.__client = None
        self.__connection = None

    
    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__connection = self.__client[self.__db_name]


    def get_db_connection(self):
        return self.__connection


    def get_db_client(self):
        return self.__client
    