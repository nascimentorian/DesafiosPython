n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
media = (n1 + n2) / 2
print(f'Sua média é : {media}')
if media < 5:
    print('Sua média é menor do que 5, REPROVADO!')
elif media > 5 and media < 7:
    print(f'Sua média é {media}, você está de recuperação.')  
else:
    print(f'Sua média é de: {media}, você foi APROVADO!')      