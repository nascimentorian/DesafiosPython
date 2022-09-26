while True:
    n = int(input('Quer ver a tabuada de qual valor?:'))
    t = 1
    if n < 0:
        break
    print(f'A tabuada de {n} é:')
    while t <=10:
        print(f'{n} x {t} = {n*t}')
        t+=1
print('Tabuada encerrada.')        

    
     
