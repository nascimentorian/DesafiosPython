def ficha(jog='desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')


n = str(input('Nome do jogador:'))
g = str(input('Quantos gols ele fez?:'))    
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g) 
else:
    ficha(n, g)       