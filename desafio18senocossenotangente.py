import math
a = float(input('Digite um ângulo:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'O seno de {a} é igual a : {s}, o cosseno de {a} é igual a {c}, e a tangente de {a} é igual a {t}')