media = dict()
media['nome'] = str(input('Qual é o seu nome?: '))
media['media'] = float(input('Qual é a sua média?: '))
if media['media'] < 7:
    media['situação'] = 'Reprovado'
for k,v in media.items():
    print(f' - {k} é igual a {v}')
