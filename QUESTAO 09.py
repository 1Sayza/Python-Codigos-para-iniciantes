positivos= False
while positivos == False:
    print("Insira 3 lados positivos do triangulo")
    A = int(input("Insira o lado A do triangulo: "))
    B = int(input("Insira o lado B do triangulo: "))
    C = int(input("Insira o lado C do triangulo: "))
    if A>0 and B>0 and C>0:
        positivos = True
if A == B and A == C:
    print("O triangulo é equilátero")
elif A != B and A != B and B != C:
    print("O triangulo é escaleno")
else:
    print("O triangulo é isósceles")