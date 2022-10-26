lista = []
while True:
    n = int(input('Digite um número:'))
    if n not in lista:
        lista.append(n)  
    else:
        print('Valor duplicado, não será adicionado.')      
    r = str(input('Quer continuar?[S/N]')).upper()
    if r in 'Nn':
        break
lista.sort()    
print(f'Os valores digitados em ordem crescente são: {lista}')    