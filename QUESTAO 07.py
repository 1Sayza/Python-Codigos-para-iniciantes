a = int(input('Digite o valor de "a": '))
b = int(input('Digite o valor de "b": '))
c = int(input('Digite o valor de "c": '))
if a == 0:
  print('Equação do primeiro grau.')
else:
  delta = (b**2) - (4*a*c)
  print('Delta={}'.format(delta))
  if delta >= 0:
    x1 = (-b + (delta ** 0.5)) / 2*a 
    x2 = (-b - (delta ** 0.5)) / 2*a 
    print('X1={}, x2={}'.format(x1,x2))
  else:
    print('Esta equação não possui raízes no conjunto dos números reais')

print('Fim.')