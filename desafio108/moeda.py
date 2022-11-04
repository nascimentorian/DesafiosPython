def metade(n = 0):
    return n / 2


def dobro(n = 0):
    return n * 2


def aumenta10(n = 0):
    aumento = (n*10) / 100
    n += aumento
    return n


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')
