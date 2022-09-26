valorc = float(input('Qual o valor da casa desejada?:'))
salario = float(input('Qual o valor do seu salário?:'))
anosp = int(input('Em quantos anos você irá pagar?'))
parcelas = anosp * 12
prestaçãomensal = valorc / parcelas
if prestaçãomensal > salario * 30 / 100:
    print('Você não pode pagar por essa casa.')
else:
    print('Seu empréstimo bancário foi aprovado!')    