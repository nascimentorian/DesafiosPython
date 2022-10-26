lista = []
nd = 0
v5 = ''
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    nd +=1
    r = str(input('Quer continuar?[S/N]:'))
    if r in 'Nn':
        break
lista.sort(reverse =True)    
print(f'Foram digitados {len(lista)} valores')    
print(f'A lista de valores ordenada de forma decrescente é: {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista')    