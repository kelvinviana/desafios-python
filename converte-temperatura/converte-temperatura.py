# Converte temperatura em graus Celsius para graus Fahrenheit e vice-versa

def celsius_fahrenheit (celsius):
    return (9/5)*celsius + 32

def fahrenheit_celsius (fahrenheit):
    return (fahrenheit - 32)*(5/9)

menu = '''

Digite o número que corresponde ao tipo de conversão que deseja realizar:

[1] - Converter Celsius para Fahrenheit
[2] - Converter Fahrenheit para Celsius

[0] - Sair

'''

while True:
    opcao = input(menu)

    if opcao == "1":
        temperatura_celsius = float(input("\nDigite a temperatura em graus Celsius:\n"))
        temperatura_fahrenheit = celsius_fahrenheit(temperatura_celsius)
        print(f"\nA temperatura {temperatura_celsius:.2f}°C convertida em graus Fahrenheit é: {temperatura_fahrenheit:.2f}°F")

    elif opcao == "2":
        temperatura_fahrenheit = float(input("\nDigite a temperatura em graus Fahrenheit:\n"))
        temperatura_celsius = fahrenheit_celsius(temperatura_fahrenheit)
        print(f"\nA temperatura {temperatura_fahrenheit:.2f}°F convertida em graus Celsius é: {temperatura_celsius:.2f}°C")

    elif opcao == "0":
        break

    else:
        print("Opção inválida!\nTente novamente!")