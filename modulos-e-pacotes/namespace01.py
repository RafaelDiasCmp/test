def funcao1():
    print(' ...início da função 1')
    if criterio == 'alterar': # LOCAL
        valor = 999
    print(f' ...valor dentro da função 1 = {valor}')

def funcao2():
    print(' ...início da função 2')
    global valor # GLOBAL
    if criterio == 'alterar': 
        valor = 999
    print(f' ...valor dentro da função 2 = {valor}')


criterio = 'alterar' # GLOBAL
valor = 10
print(f'Programa principal! Valor = {valor} (antes função 1)')

funcao1()

print(f'Programa principal! Valor = {valor} (após função 1)\n')

print(f'Programa principal! Valor = {valor} (antes função 2)')

funcao2()

print(f'Programa principal! Valor = {valor} (após função 2)')