# Desafio

# Crie um programa que pergunte ao usuário se ele deseja converter o número de registro de um material para hexadecimal ou se ele deseja converter o número hexadecimal em número de registro (um número inteiro).

# Em seguida, converta esse número em sua respectiva conversão e imprima na tela.

while True:
    opcao = input('''
Digite a opção desejada de conversão:
[1] - Converte Inteiro para Hexadecimal
[2] - Converte Hexadecimal para Inteiro

[0] - Sair

''')
    
    if opcao == "0":
        break

    elif opcao == "1":
        num = int(input("Digite o número do tipo Inteiro: "))
        print(f"O número inteiro {num} convertido em hexadecimal é: {num:X}")

    elif opcao == "2":
        num_hex = input("Digite o número do tipo Hexadecimal: ")
        num_inteiro = int(num_hex, 16)
        print(f"O número hexadecimal {num_hex.upper()} convertido em inteiro é: {num_inteiro}")

    else:
        print("Opção inválida! Tente novamente!")