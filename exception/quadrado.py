def Quadrado(dados):
    if not isinstance(dados, list) and not isinstance(dados, tuple):
        raise TypeError(f'Erro! Lista esperado, encontrado {type(dados)}')
    if not all(isinstance(x, int | float) for x in dados):
        raise ValueError('Os elementos devem ser todos numéricos')
    return [v**2 for v in dados]

l = []

i = int(input('\nDigite o número de elementos na lista: \n'))

while i > 0:
    n = input('\nDigite o valor númerico: \n')
    l.append(n)
    i -= 1

print(l)

print(Quadrado(l))

