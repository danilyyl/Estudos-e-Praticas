#Calculadora simples com condicional

print("Bem vindo(a) a minha calculadora simples!")



while True:
    entrada = input("Digite o primeiro número (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        print("Encerrando...")
        break

    N1 = int(entrada)
    N2 = int(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")


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