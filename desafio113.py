def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('ERRO! Por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0 

        else:
            return n    


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('ERRO! Por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0 

        else:
            return n             


n1 = leiaInt('Digite um número:')
n2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}')