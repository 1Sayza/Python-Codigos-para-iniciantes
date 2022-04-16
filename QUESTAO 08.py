positivos,somaangulo = False,0
while positivos == False and somaangulo != 180:
    print("Insira 3 angulos positivos cujo a soma seja igual a 180 graus")
    A = int(input("Insira o angulo A do triangulo: "))
    B = int(input("Insira o angulo B do triangulo: "))
    C = int(input("Insira o angulo C do triangulo: "))
    if A > 0 and B > 0 and C > 0:
        positivos = True
    somaangulo = A + B +C
if A < 90 and B < 90 and C < 90:
    print("O triangulo é Acutângulo")
elif A > 90 or B > 90 or C > 90:
    print("O triangulo é Obtusângulo")
elif A == 90 or B == 90 or C == 90:
    print("O triangulo é retângulo")