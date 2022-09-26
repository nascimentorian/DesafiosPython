import random
computador = random.randint(0,10)
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?'))
    tentativas +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente')
print(f'Você acertou!Você teve que usar {tentativas} tentativas para acertar')      
  