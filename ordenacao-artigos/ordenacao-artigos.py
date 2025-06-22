# Dada a lista de artigos:

# Crie uma função para ordenar a lista de artigos por data de publicação, do mais antigo ao mais recente.

from datetime import datetime, date

artigos = [
{'titulo': 'Applications of Artificial Intelligence in Academic Libraries',
'autores': ['Vijayakumar, S.','Sheshadri,K.N.'],
'data_publicacao': '16/05/2019',
'consultas': 569},
{'titulo': 'Data science in data librarianship: Core competencies of a data librarian',
'autores': ['Semeler, A. R.','Pinto, A. L.','Rozados, H. B. F.'],
'data_publicacao': '26/11/2019',
'consultas': 1004},
{'titulo': 'Data scientist: the sexiest job of the 21st century',
'autores': ['Davenport,T.H.','Patil, D J'],
'data_publicacao': '01/10/2012',
'consultas': 10231},
{'titulo': 'Bibliometria: evolução histórica e questões atuais',
'autores': ['Araújo,C.A.A.'],
'data_publicacao': '10/12/2006',
'consultas': 650}
]

# Reordena os elementos da lista 'artigos' em ordem crescente por data
artigos.sort(key=lambda artigo: datetime.strptime(artigo['data_publicacao'], '%d/%m/%Y'))

# Imprime os dados de cada artigo conforme ordem definida na linha de código acima
for artigo in artigos:
    print(f"Título: {artigo['titulo']}")
    print(f"Autores: {', '.join(artigo['autores'])}")
    print(f"Data de Publicação: {artigo['data_publicacao']}")
    print(f"Número de Consultas: {artigo['consultas']}\n")