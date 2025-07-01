def eh_palindromo(palavra):
    palavra_sem_espaco = ""

    for letra in palavra:
        if letra.isalnum():
            palavra_sem_espaco += letra

    palavra_invertida = palavra_sem_espaco[::-1]

    if palavra_sem_espaco == palavra_invertida:
        print("É palíndromo")
    else:
        print("Não é palíndromo")
    

palavra = input().lower().strip()

eh_palindromo(palavra)