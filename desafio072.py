n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:    
    digite = int(input('Digite um número de 0 até 20:'))
    if digite <=20 and digite >=0:
        break 
print(f'Você digitou o número {n[digite]}')

