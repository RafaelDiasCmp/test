def filtro(dados, pMin, pMax):
    for valor in dados:
        if pMin <= valor <=pMax:
            yield valor, valor * 1.1

precos = [36.3, 174.19, 43.71, 108.32, 89.14]

lMin = int(input('\nDigite o valor mínimo: '))
lMax = int(input('\nDigite o valor máximo: '))

for valores in filtro(precos, lMin, lMax):
    print(valores)

print('\nFim do programa\n')
