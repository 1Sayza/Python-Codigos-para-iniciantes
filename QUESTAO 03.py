ano = int(input("Digite um ano entre 1900 e 2100: "))
if ano >= 900 and ano <= 2100:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("O ano {} é Bissexto".format(ano))
    else:
        print("O ano {} Não é Bissexto".format(ano))
else:
    print('Informe o ano entre 1900 e 2100 por favor')

    