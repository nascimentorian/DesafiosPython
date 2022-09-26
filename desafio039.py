import datetime
anonascimento = int(input('Qual seu ano de nascimento?:'))
idade = datetime.date.today().year - anonascimento
idadea = 18
if idade < 18:
    print(f'Você ainda não pode se alistar, mas faltam {idadea - idade} anos para você se alistar.')
elif idade == 18:
    print('Sua idade é igual a 18, você é obrigado a se alistar.')
else:
    print(f'Se você ainda não se alistou, vocẽ já passou do tempo de se alistar, já se passaram {idade - idadea} anos desde a idade correta para alistamento.')        