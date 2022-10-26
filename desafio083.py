expressao = str(input('Digite uma expressão'))
pilha = []

for simble in expressao:
    if simble == '(':
        pilha.append('(')
    elif simble ==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break    
if len(pilha) == 0:
    print('Sua expressão é valida.')
else:
    print('Sua expressão está inválida.')                   