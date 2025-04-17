#Calculadora simples

N1 = int(input("Digite o primeiro numero: "))
N2 = int(input("Digite o segundo numero: "))
operacao = input("Digite a operação desejada, +, -, *, /: ")

if operacao == "+":
    print (N1 + N2)
elif operacao == "-":
    print (N1 - N2)
elif operacao == "*":
    print(N1 * N2)
elif operacao == "/":
    if N2 != 0:
        print(N1 / N2)
    else:
        print("Não é possivel dividir por zero.")
else:
    print("Operação inválida")

