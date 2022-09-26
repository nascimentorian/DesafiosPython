peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso / altura ** 2
if imc <= 18.4:
    print('Você está abaixo do peso.')
elif imc >=18.5 and imc <=25:
    print('Você está no peso ideal.')
elif imc >=25 and imc <=30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc <=40:
    print('Você está obeso.')
else: 
    print('Você está obeso mórbido.')            