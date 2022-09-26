
menores = 0
maiores = 0
for r in range(1,8):
    ano = int(input(f'Em que ano a {r}ª pessoa nasceu?'))
    idade = 2022 - ano    
    if idade < 18:
        menores +=1
    else:
        maiores += 1    
print(f'Existem {maiores} maiores de idade e existem {menores} de idade')        



