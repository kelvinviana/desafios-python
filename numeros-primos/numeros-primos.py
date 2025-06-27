# Recebe um número e retorna uma lista dos números primos até o número indicado, além de contar quantos números primos existem até o número dado.

def conta_restos (numero):
    """Conta quantos restos zero existem de um número até 1.

    Args:
        numero (int): Valor máximo para exibição dos números primos.

    Returns:
        Quantos restos zero o número tem até a divisão por 1. Vai ser útil pra dizer se um número é primo ou não.
    """
    divisor = numero
    contador_resto = 0
    while divisor > 0:
        resto = numero % divisor
        if resto == 0:
            contador_resto += 1
        divisor -= 1
    return contador_resto

def numeros_primos (numero):
    """Avalia se um número é primo, ou seja, só é divisível (resto zero) por ele mesmo e por 1

    Args:
        numero (int): Valor máximo até onde irá verificar se o número é primo ou não

    Returns:
        Lista: com números primos
    """
    numeros_primos = []
    for x in range(2,numero+1):
        restos = conta_restos(x)
        if restos >= 0 and restos <= 2:
            numeros_primos.append(x)
    return numeros_primos

def imprime_numeros_primos (numero):
    """Exibe os números primos até um número limite e o total encontrado.

    Args:
        numero (int): Valor máximo para exibição dos números primos.
    """
    lista_numeros_primos = numeros_primos(numero)
    
    for numero_primo in lista_numeros_primos:
        print(numero_primo)

numero = int(input("Digite até qual número você deseja verificar se é primo: "))

print(f"\nA lista de números primos até {numero} é:")
imprime_numeros_primos(numero)

print(f"\nA quantidade total de números primos até o número {numero} é:", len(numeros_primos(numero)))