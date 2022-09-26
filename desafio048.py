soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        cont +=1
        soma +=c
print(f'A soma de todos os números impares e multiplos de 3 é igual a {soma}')        
print(f'O total de valores encontrados foi {cont}')
        
