import random
possibilidades = ['pedra', 'papel', 'tesoura']
computador = random.choice((possibilidades))
jogador = str(input('Digite pedra, papel ou tesoura.'))
if jogador == 'tesoura' and computador == 'papel':
    print(f'Você ganhou do computador!, o computador digitou {computador}')
elif jogador == 'tesoura' and computador == 'tesoura':
    print('Empate!') 
elif jogador ==  'tesoura' and computador == 'pedra':
    print(f'Você perdeu!, o computador digitou {computador}') 
elif jogador == 'papel' and computador == 'tesoura':
    print(f'Você perdeu o computador digitou {computador}')
elif jogador == 'papel' and computador == 'pedra':
    print(f'Você ganhou, o computador digitou {computador}.')  
elif jogador == 'papel' and computador == 'papel':
    print(f'Empate! o computador também digitou {computador}')  
elif jogador == 'pedra' and computador == 'papel':
    print(f'Você perdeu o computador digitou {computador}')
elif jogador == 'pedra' and computador == 'tesoura':
    print(f'Você ganhou, o computador digitou {computador}')
elif jogador == 'pedra' and computador == 'pedra':
    print(f'Empate! O computador também digitou {computador}')               

print('Fim do jogo, espera que tenha se divertido!')   