from time import sleep
from random import randint
def sorteia(lista):
    print('Sorteando 5 valores da lista:', end= '')
    for c in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end= ' ')
        sleep(0.4)


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 ==0:
            soma += c
    print(f'A soma dos valores pares de {lista} são: {soma}')        


numeros = []
sorteia(numeros)
somaPar(numeros)
            