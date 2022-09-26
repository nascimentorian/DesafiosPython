n1 = int(input('Primeiro número:'))
n2 = int(input('Digite o segundo número:'))
opção = 0
while opção != 5:
    dados = int(input(print('''
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa''')))
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        multiplicação = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a: {multiplicação}')
    elif opção == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        elif n2 > n1: 
            maior = n2   
        print(f'O sinal maior entre {n1} e {n2} é: {maior}')  
    elif opção == 4:
        print('Digite os valores novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opção == 5:
        print('Finalizando') 
    else:
        print('Opção inválida, verifique os dados e tente novamente.')           
        
print('Fim do programa, volte sempre!')    