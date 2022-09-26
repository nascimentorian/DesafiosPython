tot18 = 0
toth = 0
m20 = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    if idade >=18:
        tot18+=1
    if sexo == 'M':
        toth +=1
    if sexo == 'F' and idade < 20:
            m20 +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos : {tot18}')
print(f'Ao todo temos o total de {toth} homens cadastrados')
print(f'Ao todo temos um total de {m20} mulheres com menos de 20 anos')
    

