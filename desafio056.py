somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'------ {p}ª PESSOA ------')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome    
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1    
print(f'A média da idade de todos é: {somaidade / 4 }')    
print(f'O homem mais velho tem {maioridadehomem} anos e o nome dele é {nomevelho}')
print(f'O total de mulheres com menos de 20 anos é : {totmulher20}')