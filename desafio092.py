from datetime import datetime
funcionario = {}
funcionario['nome'] = str(input('Nome: '))
funcionario['anonascimento'] = datetime.now().year -  int(input('Ano de nascimento: '))
funcionario['carteira'] = int(input('Carteira de trabalho: [0 não tem]:'))
if funcionario['carteira'] != 0:
    funcionario['anocontratacao'] = int(input('Ano de contratação: '))
    funcionario['salario'] = float(input('Salário: '))  
    funcionario['aposentadoria'] = funcionario['anonascimento'] + ((funcionario['anocontratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for i, v in funcionario.items():
    print(f'  - {i} tem o valor {v}')