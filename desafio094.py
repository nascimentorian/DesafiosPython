galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input(('Sexo: [M/F]'))).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, apenas digite M ou F') 
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy()) 
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]   
        if resposta in 'SN':
            break 
        print('Erro, responda apenas S OU N.')
    if resposta == 'N':
        break      
print(galera)
print(f'Ao todos temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f' A média de idade é de {media:5.2f} anos. ')
print(f'As mulheres cadastradas foram ', end= '')
for p in galera: 
    if p['sexo'] == 'F':
        print(f' {p["nome"]}', end= '')
print()  
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')    
        print()
print('<< ENCERRADO >>')              