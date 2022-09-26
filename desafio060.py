from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = factorial(n)
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else '=', end= '')
    c-=1
print(f'{f}')    
#print(f'O fatorial de {n} é: {f}',end='')