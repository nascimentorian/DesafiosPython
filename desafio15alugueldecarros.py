km = float(input('Qual foi a quantidade de kilometros percorridos?'))
dias = int(input('Por quantos dias o carro foi alugado?'))
pagod = dias * 60
pagok = km * 0.15
print(f'O valor a ser pago é igual a : {pagod + pagok}')