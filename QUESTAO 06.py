peso = int(input("Digite seu peso em Kg (ex: 75): "))
altura = float(input("Digite sua altura em metros (ex: 1.67): "))
IMC = peso/pow(altura,2)

if IMC < 18.5:
    print("Voce esta abaixo do peso")
elif IMC>=18.5 and IMC <= 24.9:
    print("Seu peso está normal")
elif IMC>24.9 and IMC <= 29.9:
    print("Voce esta com sobrepeso")
elif IMC>29.9 and IMC <= 34.9:
    print("Voce esta com Obesidade Grau 1")
elif IMC>34.9 and IMC <= 39.9:
    print("Voce esta com Obesidade Grau 2")
elif IMC>39.9:
    print("Voce esta com Obesidade Grau 3 ou morbida")