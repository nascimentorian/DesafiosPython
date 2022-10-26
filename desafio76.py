lista = ('Lápis', 1.50,
        'Borracha', 1.30,
        'Lapiseira', 2.50,
        'Caneta', 1.60      )
for pos in range(0, len(lista)):
    if pos % 2 ==0:
        print(f'{lista[pos]}') 
    else:
        print(f'R${lista[pos]}')              