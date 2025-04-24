#Números pares até N

print("Neste programa voçe irá digitar um numero inteiro " \
"e eu vou mostrar desse numero os numeros pares, vamos começar? ")

n = int(input("Digite um numero inteiro: "))

for i in range(n + 1):
    if i % 2 == 0:
        print(i)

print("Muito obrigado por ter usado este programa!")