#Verificação se o numero digitado pelo usuario é par ou ímpar

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("O seu numero digitado é par!")
else:
    print("Seu numero é impar!")