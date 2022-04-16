numero = int(input("Digite um número: "))
if numero % 2 == 0:
    if numero > 0:
        print("O número é um par positivo")
    else:
        print("O número é um par negativo")
if numero % 2 != 0:
    if numero > 0:
        print("O número é um ímpar positivo")
    else:
        print("O número é um ímpar negativo")
if numero == 0:
    print("O número é nulo")
        
