def gerador_pares():
    a = 2
    while True:
        yield a
        a += 2

gen = gerador_pares()  # Corrigido para instanciar o gerador

for _ in range(15):
    print(next(gen), end=' ')
