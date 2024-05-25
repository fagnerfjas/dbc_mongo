from models.connections.mongo_connect import DbConnectionManager 
from models.repository.DisciplinaRepository import DisciplinaRepository

db_adm = DbConnectionManager()
db_adm.connect_to_db()
connection = db_adm.get_db_connection()

disciplinas_repository = DisciplinaRepository(connection)

nova_disciplina = {
    'nome': 'Artes',
    'cod': 'ND',
    'horario': 35,
    'cursos': {
        'cod': 'cursos aleatorios',
        'dict': 'Dicionário de cursos'
    }
}
#disciplinas_repository.insert_document(nova_disciplina)

#dados = disciplinas_repository.select_documents({'nome': "Artes", 'cursos.cod': 'cursos aleatorios'})
#print(dados)

#dados = disciplinas_repository.select_one({'nome': "Artes", 'cursos.cod': 'cursos aleatorios'})
#dados = disciplinas_repository.select_if_property_exist('cod')
dados = disciplinas_repository.select_meny_order({'cargaHoraria': { '$exists': True}}, [('carca', -1)])
print(dados)


# nova_disciplina = {
#     'nome': 'Nova disciplina',
#     'cod': 'ND',
#     'horario': 35,
#     'cursos': {
#         'cod': 'cursos aleatorios',
#         'dict': 'Dicionário de cursos'
#     }
# }

# list_documents = [
#     {'nome': 'dict1'},
#     {'nome': 'dict2'},
#     {'nome': 'dict3'},
#     {'nome': 'dict4'}
# ]

# disciplinas_repository.insert_document(nova_disciplina)

# disciplinas_repository.insert_documents(list_documents)


# elements = connection2.get_collection('disciplinas')
# elements.insert_one({
#     'nome': 'Nome da disciplina',
#     'cod': 'Codigo da disicplina',
#     'horario': 'horario da disciplina'
# })

# elements_filter = elements.find({})

# print(elements_filter)

# for item in elements_filter: 
#     print(item)
