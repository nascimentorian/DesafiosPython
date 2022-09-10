velocidade = float(input('Velocidade do carro:'))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você foi multado, o valor da sua multa é igual a: {multa}')
else:
   print('Você está dentro  das normas!')   

