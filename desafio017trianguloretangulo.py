import math
co = float(input('Qual é a medida do seu cateto oposto?'))
ca = float(input('Qual é a medida do seu cateto adjacente?'))
h1 = (co**2 + ca**2)
h2 = math.sqrt(h1)
print(f'O comprimento da hipotenusa é igual a : {h2} ' )