lista = [12, 26, 65, 87, None]

for valor in lista:
    if bool(valor) == True:
        print(f'{valor} é um número válido')
    else:
        print('É um valor vazio')


