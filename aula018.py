galera = list()
dado = list()
totma = 0
totm = 0
for c in range(0,3):
    dado.append(str(input('Digite seu nome:')))
    dado.append(int(input('Digite sua idade:')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')  
        totma +=1 
    else:
        print(f'{p[0]} é menor de idade')    
        totm +=1
print(f'Temos {totma} maiores e {totm} menores de idade.')        