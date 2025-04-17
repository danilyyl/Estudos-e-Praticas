#Verificação se o numero digitado pelo usuario é par ou ímpar com condicional

while True:
    numero = int(input("Digite um numero(ou 0 para sair): "))

    if numero == 0:
        print("Encerrando...")
        break

    if numero % 2 == 0:
        print("Seu numero é par!")
    else:
        print("Seu numero é impar!")