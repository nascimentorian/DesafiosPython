temp = []
principal = []

while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    principal.append(temp[:])
    temp.clear()
    
    continuar = str(input('Quer continuar?[S/N]:'))
    if continuar in 'Nn':
        break
print(f'Os dados foram {principal}')    
print(f'Ao todo foram registradas {len(principal)} pessoas')
print(f'O maior peso foi {max(principal)}')
print(f'O menor peso foi {min(principal)}')