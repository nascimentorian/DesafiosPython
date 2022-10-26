valores = (int(input('Digite um número:')), int(input('Digite outro número:')), int(input('Digite um outro número:')), int(input('Digite outro número:')), int(input('Digite um último número:')))
pares = ()
print(f'Você digitou os valor {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na posição {valores.index(3)+1}')
else:
    print(f'O  valor 3 não foi encontrado.')    
print(f'Os números sorteados pares foram:', end='')
for n in valores:
    if n % 2 ==0:
        print(n , end=' ')