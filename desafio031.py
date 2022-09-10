distancia = float(input('Qual será a distância da sua viagem?'))
if distancia < 200:
    print(f'O preço da sua passagem é:{distancia * 0.50}')
else:
    print(f'O valor da sua passagem é: {distancia * 0.45}')    