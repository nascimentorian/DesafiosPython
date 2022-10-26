lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número:')))
    r = str(input('Quer continuar? [S/N]:'))
    if r in 'Nn':
        break
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
print(f'A lista completa é: {lista}')        
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')              