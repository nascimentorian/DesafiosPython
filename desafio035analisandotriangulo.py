r1 = int(input('Digite o tamanho da primeira reta'))
r2 = int(input('Digite o tamanho da segunda reta:'))
r3 = int(input('Digite o tamanho da terceira reta:'))
if r1< r2 + r3 and r2< r1+r3 and r3< r2 + r1:
    print('você pode formar um triângulo!')
else:
    print('Você não pode formar um triângulo!')    