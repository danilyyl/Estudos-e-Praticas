''' Objetivo: Verificar se uma palavra é um palíndromo 
(se ela pode ser lida da mesma forma de trás para frente).'''

while True:
    palavra = input("Digite uma palavra que possa ser lida da mesma forma de trás para frente ou digite (sair) para encerrar: ")
    if palavra == "sair":
        print("Encerrando...")
        break

    elif not palavra.isalpha():
        print("❗Por favor, digite apenas palavras (sem números ou símbolos).")
        continue
    
    print("Você digitou:", palavra)
    print("Agora estou verificando se ela pode ser invertida e lida da mesma forma de tras para frente...")
    resultado = palavra[::-1]

    if palavra == resultado:
        print("Sim!, essa palavra é um palindromo")
    else:
        print("opss!, não essa palavra não é um palindromo, tente novamente")

        