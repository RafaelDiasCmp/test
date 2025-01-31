# Módulo como script
def soma(*args):
    r = 0
    for x in args:
        r += x
    return r

def mult(*args):
    r = 1
    for x in args:
        r *= x
    return r

if '__name__' == '__main__': # se esse for o programa principal...
    print('Início do módulo')