pt = int(input('Digite o primeiro termo de uma PA:'))
rz = int(input('Digite a razão de uma PA:'))
termo = pt
cont = 1
while cont <=10:
    print(f'{termo}', end=' ')  
    termo += rz
    cont += 1
    
    
