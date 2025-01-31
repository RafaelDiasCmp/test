def Paridade(pValor):
    
    #if not isinstance(pValor, int):
    #    raise Exception('A função deve receber um int')
    if type (pValor) != int:
        raise Exception('A função deve receber um int')
    else:
        if pValor % 2 == 0:
            return 'PAR'
        else:
            return 'ÍMPAR'
    
    
n = int(input('Digite algo: '))
r = Paridade(n)

print(f'{n} é {r}')