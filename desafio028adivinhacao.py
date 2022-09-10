import random

numero = (random.randint(0,5))
nc = int(input('Chute um número e tente acertar!'))
if nc == numero:
    print('Parabéns, você acertou!')
else:
    print('Você errou, tente novamente!')