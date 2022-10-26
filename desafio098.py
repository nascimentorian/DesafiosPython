from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1 
    print('=-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}!')

       

    if i < f:
        cont = i 
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p 
            sleep(0.5)  
        print('FIM!') 
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(0.5)
        print('FIM')   
      

contador(1,10,1)
contador(10,0,2)
print('-=' * 20)
print(f'Personalize a contagem:')
inicio = int(input('Inicio: '))
fim = int(input('Fim:  '))   
passo = int(input('Passo:'))
contador(inicio,fim,passo)    