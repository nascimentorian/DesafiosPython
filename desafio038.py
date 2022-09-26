numero1 = int(input('Primeiro número:'))
numero2 = int(input('Segundo número:'))
if numero1 > numero2:
    print(f'O número {numero1} é maior do que {numero2}.')
elif numero2 > numero1:
    print(f'O número {numero2} é maior do que o {numero1}.')  
else:
    print('Não existe valor maior, os dois são iguais.')      