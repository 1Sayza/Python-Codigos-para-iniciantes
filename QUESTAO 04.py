x = int(input("Digite a coordenada X do ponto: "))
y = int(input("Digite a coordenada Y do ponto: "))

if x >= 0:
    if y >= 0:
        print("O ponto está no primeiro quadrante")
    else:
        print("O ponto está no quarto quadrante")
else:
    if y >= 0:
        print("O ponto está no segundo quadrante")
    else:
        print("O ponto está no terceiro quadrante")