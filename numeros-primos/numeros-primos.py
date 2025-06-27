# Recebe um número e retorna uma lista dos números primos até o número indicado, além de contar quantos números primos existem até o número dado.

# Versão otimizada, evitando cálculos desnecessários e utiliza melhor os conceitos matemáticos que determinam se um número é primo ou não.

def conta_divisores(numero):
    """Conta a quantidade de divisores inteiros positivos de um número.

    Realiza a contagem de divisores de forma otimizada, verificando apenas até
    a raiz quadrada do número e contando pares de divisores.

    Args:
        numero (int): O número inteiro positivo a ser analisado.

    Returns:
        int: Quantidade total de divisores do número.
             Retorna 0 se o número for menor que 2.

    Examples:
        >>> conta_divisores(7)
        2
        >>> conta_divisores(12)
        6
    """
    if numero < 2:
        return 0
    contador = 2  # 1 e o próprio número
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            if divisor == numero // divisor:  # Caso de quadrado perfeito
                contador += 1
            else:
                contador += 2
    return contador


def encontra_primos(limite):
    """Gera uma lista de números primos até um determinado limite.

    Utiliza a função conta_divisores() para identificar números primos de forma
    eficiente, considerando apenas números ímpares após o 2.

    Args:
        limite (int): Valor máximo (inclusive) para a busca de números primos.

    Returns:
        list: Lista contendo todos os números primos encontrados até o limite,
              em ordem crescente. Retorna lista vazia se limite < 2.

    Raises:
        TypeError: Se o limite não for um número inteiro.

    Examples:
        >>> encontra_primos(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if not isinstance(limite, int):
        raise TypeError("O limite deve ser um número inteiro")
    
    if limite < 2:
        return []
    
    primos = [2]
    for candidato in range(3, limite + 1, 2):  # Verifica apenas ímpares
        if conta_divisores(candidato) == 2:
            primos.append(candidato)
    return primos


def imprime_primos(limite):
    """Exibe os números primos até um limite e o total encontrado.

    Formata a saída para mostrar os números primos separados por vírgula
    e o total de primos encontrados.

    Args:
        limite (int): Valor máximo para exibição dos números primos.

    Examples:
        >>> imprime_primos(10)
        Números primos até 10:
        2, 3, 5, 7
        Total de primos encontrados: 4
    """
    primos = encontra_primos(limite)
    print(f"\nNúmeros primos até {limite}:")
    print(*primos, sep=', ')
    print(f"\nTotal de primos encontrados: {len(primos)}")


def main():
    """Função principal que orquestra a execução do programa.

    Solicita entrada do usuário, valida o valor informado e executa
    a exibição dos números primos até o limite especificado.

    Trata erros de entrada e fornece feedback adequado ao usuário.
    """
    try:
        limite = int(input("Digite até qual número deseja verificar primos: "))
        if limite < 2:
            print("Por favor, digite um número maior ou igual a 2.")
            return
        imprime_primos(limite)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()