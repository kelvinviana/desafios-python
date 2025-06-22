# Crie um programa que solicite ao usuário que digite o número total de páginas de um livro e o número de páginas que foram lidas, e em seguida, calcule e imprima a porcentagem do livro que foi lida até o momento.

# Caso o usuário insira um número errado de páginas lidas (maior do que o número de páginas do livro), o programa deve continuar pedindo o número de páginas lidas até que o usuário indique que terminou de ler o livro, ou seja, tenha lido todas as páginas.

from decimal import Decimal

total_paginas = Decimal(int(input("Digite o número total de páginas do livro: ")))
paginas_lidas = Decimal(int(input("Digite o número de páginas lidas: ")))

while(paginas_lidas > total_paginas):
    paginas_lidas = Decimal(int(input("Digite o número de páginas lidas: ")))

percentual_lido = (paginas_lidas / total_paginas) * 100

print(f"{percentual_lido:.2f}% do livro foi lido até o momento.")

if paginas_lidas == total_paginas:
    print("Parabéns por ter concluído a leitura do livro!")