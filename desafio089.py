ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2 ) / 2
    ficha.append([nome, [nota1,nota2], media])
    continuar = str(input('Quer continuar?[S/N]'))
    if continuar in 'Nn':
        break
for i, a in enumerate(ficha):
    print(f'{i}{a[0]}{a[2]}')
while True:
    opc = int(input('Mostrar notas de qual aluno?999 interrompe '))    
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')