def fg():
    resto = 0
    num = 2
    while True:
        if num % 2 == resto:
            dado = (yield num) #yield como expressão
            if dado is not None: #quando a função não está sendo usada em uma iteração
                if dado not in (0, 1):
                    raise ValueError(f'Esperado 0 ou 1 - foi passado {dado}')
                resto = dado
                num = 0
        num += 1

gen = fg()

# 5 valores pares
print('\nGera 5 valores pares')

for _ in range(5):
    print(next(gen), end =' ')

# 5 valores ímpares
print('\n\nGera 5 valores ímpares')

ret = gen.send(1)
print(ret, end=' ')

for _ in range(4):
    print(next(gen), end =' ')

# 8 pares
print('\n\nGera 8 valores pares')
ret = gen.send(0)
print(ret, end=' ')
for _ in range(7):
    print(next(gen), end =' ')

#ret = gen.send(2)
#gera o ValueError

print('\n\nFim do programa\n')