salario = float(input('Qual é o seu salário?'))
if salario > 1250:
    salarioa1 = (salario * 10) / 100
    print(f'Seu aumento é de : {salarioa1}R$, ficando:{salarioa1 + salario}R$')
else:
    salarioa2 = (salario *15)/ 100
    print(f'Seu aumento foi de {salarioa2}R$, ficando: {salarioa2 + salario}R$')   