#Verificação se o numero1 é maior, igual ou menor que numero2

n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite um segundo numero inteiro: "))

if n1 > n2:
    print("{} é maior que {}".format(n1,n2))
elif n1 == n2:
    print("{} é igual a {}".format(n1,n2))
else:
    print("{} é menor que {}".format(n1,n2))