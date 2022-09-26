sexo = str(input('Digite o seu sexo, [M/F]:')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, digite novamente.')).strip().upper()
print('Dados salvos com sucesso.')    
