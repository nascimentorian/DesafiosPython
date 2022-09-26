resp = 'S'
total = 0
soma = 0
maior = 0
menor = 0

while resp == 'S':
    n = int(input('Digite um número inteiro: '))
    resp = str(input('Quer continuar?: [S/N]')).upper().strip()
    soma += n
    total += 1
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n        

media = soma / total    
print(f'A média dos valores é {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')
    
