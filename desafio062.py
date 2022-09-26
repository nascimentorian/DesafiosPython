pt = int(input('Digite o primeiro termo de uma PA:'))
rz = int(input('Digite a razão de uma PA:'))
termo = pt
cont = 1
total = 0
maistermos = 10
while maistermos != 0:
    total += maistermos
    while cont <=total:
        print(f'{termo}', end=' ')  
        termo += rz
        cont += 1
    print('Pausa')
    maistermos = int(input('Quantos termos você quer mostrar a mais?:'))
    