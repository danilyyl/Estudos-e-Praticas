# fatorial de um numero
digite = int(input("Digite um numero: "))

resultado = 1

for numero in range(1, digite + 1):
    resultado *= numero

    print("o fatorial do seu numero digitado é: ", resultado)
    

