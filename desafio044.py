preço = float(input('Digite o preço das compras:'))
print('''Formas de pagamento 
[1]à vista dinheiro/cheque
[2]à vista cartão
[3]Parcelado 2x cartão
[4])Parcelado 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    preço2 = preço - preço * 10 / 100
    print(f'O valor do produto com desconto de 10% ficou: {preço2}')
elif opção == 2:
    preço2 = preço - preço * 5 / 100
    print(f'O valor do seu produto com desconto de 5% ficou igual a {preço2}')  
elif opção == 3:
    print('Você não obteve desconto.')
elif opção == 4:
    preço2 = preço + preço * 20 / 100
    print(f'O preço do seu produto com os juros ficou igual a : {preço2}')    
