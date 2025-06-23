# ORDENAR TITULOS
# '''
# Desafio:

# O desafio consiste em ordenar uma lista de títulos de livros em ordem alfabética e deixá-los separados por vírgula.
# A lista de títulos é fornecida como uma string chamada "titulos", onde cada título está em uma nova linha.


# Segue exemplo de lista:
# O Senhor dos Anéis
# Harry Potter e a Pedra Filosofal
# 1984
# O Lobo da Estepe
# Cem Anos de Solidão
# A Metamorfose
# A Revolução dos Bichos
# Crime e Castigo
# Macunaíma

# '''

def ordenar_titulos(titulos):
    titulos_lista = titulos.strip().split("\n")
    titulos_ordenados = sorted(titulos_lista)
    return titulos_ordenados

titulos = '''
O Senhor dos Anéis
Harry Potter e a Pedra Filosofal
1984
O Lobo da Estepe
Cem Anos de Solidão
A Metamorfose
A Revolução dos Bichos
Crime e Castigo
Macunaíma
'''

titulos_ordenados = ordenar_titulos(titulos)

print(", ".join(titulos_ordenados))