import random
v = 0
while True:
    jogador = int(input('Diga um valor de 1 até 10:'))
    computador = random.randint(1,10)
    total = jogador + computador
    iop = str(input('Par ou impar?[P/I]:')).upper().strip()
    if iop == 'P':
        if jogador + computador % 2 == 0:
            print(f'Você ganhou, o computador jogou:{computador}.')
            v +=1
        else:
            print(f'Você perdeu, o computador jogou: {computador}')
            break
    if iop == 'I':
        if jogador + computador % 2 == 1:
            print(f'Você ganhou, o computador jogou {computador}.') 
            v +=1
        else:
            print(f'Você perdeu, o computador jogou: {computador}') 
            break
        print('Vamos jogador novamente!')
print(f'Você perdeu, você venceu {v} vezes.')                          
