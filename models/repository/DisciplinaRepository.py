from typing import Dict, List
    
class DisciplinaRepository: 

    def __init__(self, db_connection) -> None:
        self.__collection_name = 'disciplinas'
        self.__db_connection = db_connection

    
    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection (self.__collection_name)
        collection.insert_one(document)
        return document


    def insert_documents(self, documents: List[Dict]) -> List[Dict]: 
        collection = self.__db_connection.get_collection (self.__collection_name)
        collection.insert_many(documents)
        return documents


    def select_documents(self, filter) -> List[Dict]: 
        collection = self.__db_connection.get_collection (self.__collection_name)
        data = collection.find(filter,
            {
                '_id': 0}
            )
        response = []
        for doc in data:
            response.append(doc)
        return response
    

    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one( filter, {'_id': 0} ) 
        return data
    

    def select_if_property_exist(self, property) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({property: {'$exists': True}})
        response = []
        for elem in data: 
            response.append(elem)
        return response
    
    
    def select_meny_order(self, filter, params_sort):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            filter,
            {'_id': 0}
        ).sort( params_sort )

        for elem in data: print(elem)