vogais = ('CARRO','CANETA', 'GARRAFA', 'CELULAR')
for p in vogais:
    print(f'\n Na palavra {p} temos:')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')