# Desafio:

# O desafio consiste em escrever um programa que receba o número de livros emprestados por dia de uma biblioteca ao longo de uma semana (7 dias) e calcule:

# O número total de livros emprestados na semana
# A média diária de empréstimos
# O dia com o maior número de empréstimos
# Ao final, exiba os resultados para o usuário.

dia = 1
total_livros = 0
historico_diario = []

while (dia <= 7):
    num_livros = int(input(f"Quantidade de livros emprestados no dia {dia}: "))
    historico_diario.append(num_livros)
    total_livros += num_livros
    dia += 1

media_diaria = total_livros / 7

dia_maior = max(historico_diario)

print(f"Número total de livros emprestados na semana: {total_livros}")
print(f"Média diária de empréstimos: {media_diaria:.2f}")
print(f"Dia com o maior número de empréstimos: Dia {dia_maior}")