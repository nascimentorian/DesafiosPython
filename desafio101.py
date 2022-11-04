
def vota(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Sua idade é {idade}, você não vota.'
    else:    
        return f'Sua idade é {idade}, você vota.'
    


resposta = int(input('Em que ano você nasceu?:'))
print(vota(resposta))
        