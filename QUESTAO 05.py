xa = int(input("Digite a coordenada X do ponto A: "))
ya = int(input("Digite a coordenada Y do ponto A: "))
xb = int(input("Digite a coordenada X do ponto B: "))
yb = int(input("Digite a coordenada Y do ponto B: "))

distancia = pow((pow((xb-xa),2)+pow((yb-ya),2)),1/2)
print("A distancia dos pontos é de {}".format(distancia))