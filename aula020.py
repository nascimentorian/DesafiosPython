# def titulo(txt):
#     print('-' *30)
#     print(txt)
#     print('-'* 30)


# titulo('       CURSO EM VIDEO'   )

# titulo('       APRENDENDO PYTHON')
# titulo('       OI')



# def soma(a,b):
#     s = a + b
#     print(s)


# soma(4, 5)

# soma(8,9)

# soma(2,1)


# def soma(a,b):
#     print(f'A= {a} e B = {b}')
#     s = a + b
#     print(f'A soma {a} + {b} = {s}')


# soma(4,5)

# def contador(*num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números')    
    

# contador(2 ,1 ,7)
# contador(8 ,0)
# contador(4 ,4 ,7 ,6 ,2)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos +=1


# valores = [6, 3, 8, 2, 4, 5]
# dobra(valores)
# print(valores)


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')    

soma(5,2)
soma(8,4)
