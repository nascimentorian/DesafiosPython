numerosd = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro, 999 para parar: '))
    numerosd += 1
    soma += n
soma = soma -999
print(f'Foram digitados {numerosd} números e a soma deles é igual a: {soma}')

