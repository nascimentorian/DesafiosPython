import datetime
nascimento = int(input('Digite seu ano de nascimento:'))
idade = datetime.date.today().year - nascimento
if idade <= 9:
    print(f'Você tem {idade} anos,você atua na classe mirim.')
elif idade <= 14:
    print(f'Você tem {idade} anos, você atua na classe infantil.')    
elif idade <= 19:
    print(f' você tem {idade} anos, você atua na classe JUNIOR')    
elif idade <= 25:
    print('Você pertence a classe senior.')    
else:
    print('Você atua na classe MASTER')    