from time import sleep
def maior(* valores):
    print('-='*20)
    print('ANALISANDO NUMEROS')
    for v in valores:
        print(f'{v}', end = ' ')
        sleep(0.3)
    
    print('-='*20)
    maiorn = 0
    for c in valores:
        if c > maiorn:
            maiorn = c
    print(f'O maior número é: {maiorn}' ,end=' ')
    

maior(5,3,2,1,7,6)
maior(5,7,6,1,9,2)            

