frase = str(input('Digite uma frase:')).upper().strip()
vezesaparece = frase.count('A')
print(f'A letra A aparece {vezesaparece} vezes')
primeirapos = frase.find('A')+1
print(f'A letra a aparece pela primeira vez na posição {primeirapos}')
ultimapos = frase.rfind('A')+1
print(f'A ultima vez que a letra A aparece é na posição {ultimapos}')