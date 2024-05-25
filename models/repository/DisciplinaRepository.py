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
    
    def select_documents(self) -> List[Dict]: 
        collection = self.__db_connection.get_collection (self.__collection_name)
        data = collection.find(
            {'nome': "Artes", 'cursos.cod': 'cursos aleatorios'},
            {'_id': 0}
            )

        for doc in data:
            print(doc)
            print()