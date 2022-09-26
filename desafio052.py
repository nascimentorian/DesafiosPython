np = int(input('Digite um número e verifique se ele é primo ou não:'))
tot = 0
for c in range(1,np,):
    if np % c == 0:
        tot += 1
if tot == 2:
        print('Seu número é primo')
else:
        print('Seu numero não é primo.')        