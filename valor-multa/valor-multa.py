# Desafio:

# O desafio consiste em criar um programa em Python para calcular a multa a ser paga por um usuário de biblioteca que devolveu um livro com atraso.

# Para isso, o programa deve solicitar ao usuário o número de dias que o livro foi devolvido após a data de vencimento e calcular a multa com base na seguinte tabela:

# Até 3 dias de atraso: multa de R$ 0,50 por dia de atraso

# De 4 a 7 dias de atraso: multa de R$ 1,00 por dia de atraso

# Mais de 7 dias de atraso: multa de R$ 2,00 por dia de atraso

# Ao final, o programa deve exibir a mensagem “O valor da sua multa é R$ X”, em que X é o valor da multa calculada.

num_dias = int(input("Insira o número de dias que o livro foi devolvido após a data de vencimento: "))

if num_dias <= 3:
    multa = 0.50 * num_dias

elif num_dias > 3 and num_dias <= 7:
    multa = 1.00 * num_dias

elif num_dias > 7:
    multa = 2.00 * num_dias

print(f"O valor da sua multa é R$ {multa:.2f}")