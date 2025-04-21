#tabuada
while True:
    try:
        digite = int(input("Digite um número e vou mostrar a tabuada dele: "))
        break  # Se a conversão for bem-sucedida, sai do loop
    except ValueError:
        print("Por favor, digite um número válido.")


for numero in range(1, 11):
    resultado = digite * numero
    print("{} x {} = {} ".format(digite, numero, resultado))
    
