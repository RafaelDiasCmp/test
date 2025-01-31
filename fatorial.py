# Função que recebe um número e retorna uma tupla com o número e o fatorial desse número

def funcao_fatorial():
    num, fat = 0, 1
    while True:
        yield num, fat
        num += 1
        fat *= num

N = int(input('Digite a quantidade: '))
gen = funcao_fatorial()
for _ in range(N):
    print(next(gen))

print('\nFim do programa\n')