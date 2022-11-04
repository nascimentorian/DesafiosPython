def fatorial(num, show=False):
    f = 1
    for c in range(num,0,-1):
        if show:
            print(c, end=' ')
        if c > 1:
            print(' x ', end=' ')  
        if c == 1:
            print('=', end=' ')      
        f *= c
    return f


print(fatorial(6, show=True))        
