a = int(input("Digite o primeiro valor do cateto do triângulo: "))
b = int(input("Digite o segundo valor do cateto do triângulo: "))
if a > 0 and b > 0:
   c = pow((pow(a,2)+pow(b,2)),1/2)
   print("O resultado da hipotenusa calculada do Triângulo foi {}".format(c))
else:
   print("Foi informado um valor inválido para o cálculo da Hipotenusa")