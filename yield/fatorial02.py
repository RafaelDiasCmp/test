def funcao_fatorial():
    num, fat = 0, 1
    while True:
        i = (yield num, fat)  # i recebe valor através do método send
        if i is not None:
            num, fat = i, 1
            for a in range(1, num + 1):
                fat *= a
        else:
            num += 1
            fat *= num

qtde = int(input('Digite a quantidade de fatoriais desejados: '))
gen = funcao_fatorial()
next(gen)  # Inicializa o gerador

while True:
    prim = int(input('\nDigite o valor inicial para os fatoriais (negativo para sair): '))
    if prim < 0:
        break  # Para a execução se o usuário digitar um valor negativo
    
    r = gen.send(prim)
    fatoriais = [r]

    for _ in range(qtde - 1):
        fatoriais.append(next(gen))

    print(f'\nSequência de {qtde} fatoriais iniciando em {prim}:')
    print(fatoriais)

print('\nFim do programa\n')
