totalgasto = 0
maior1000 = 0
menor = 0
cont = 0
barato = ''
while True:
    nomep  = str(input('Nome do produto:'))
    preço = float(input('Preço do produto:'))
    cont +=1
    totalgasto += preço
    if preço > 1000:
        maior1000+= 1
    if cont == 1:
        menor = preço
        barato = nomep
    else:
        if preço < menor:
            menor = preço      
            barato = nomep  
    nomepb = 0
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print(f'O total gasto foi: {totalgasto}')  
print(f'{maior1000} produtos custam mais de R$1000')  
print(f'O produto mais barato foi {barato} que custa {menor}R$.')

