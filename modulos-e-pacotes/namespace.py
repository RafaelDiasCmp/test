def soma(a, b):
    print('\nParte 3 - Namespace local - função soma\n')
    for s in dir():
        print(s)
    return a + b

def diferenca(x, y):
    print('\nParte 3 - Namespace local - função diferença\n')
    for s in dir():
        print(s)
    return x - y

print('\nParte 1 - Namespace do Interpretador Python built-in\n')
print(dir(__builtins__))

print('\nParte 2 - Namespace global do programa\n')
v1 = 10
v2 = -20

for a in dir():
    if '__' not in a:
        print(a)

resultadoSoma = soma(v1, v2)


resultadoDiferenca = diferenca(v1, v2)

print(f'{v1} + {v2} = {resultadoSoma}')
print(f'{v1} + {v2} = {resultadoDiferenca}')