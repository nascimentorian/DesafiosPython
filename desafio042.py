r1 = float(input('Digite o valor da primeira reta:'))

r2 = float(input('Digite o valor da segunda reta:'))
r3 = float(input('Digite o valor da terceira reta:'))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('Você pode formar uma reta!')
else:
    print('Você não pode formar uma reta.')
if r1 == r2 and r2 == r3:
    print('Você tem um triângulo equilatero')
elif r1 ==r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r1 or r3 == r2:
    print('Você tem um triângulo isosceles')  
elif r1 != r2 != r3 != r1:
    print('Você tem um triangulo escaleno.')    