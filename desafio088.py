from random import randint
jogos = list()
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
lista = list()
while total <=quantidade:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont +=1
        if cont >=6:
            break
    lista.sort()   
    jogos.append(lista[:])
    lista.clear() 
    total +=1
    print(f'Os numeros sorteados foram {jogos}')        