def media_movel():
    total, qtde = 0, 0
    while True:
        novo_dado = (yield total / qtde if qtde > 0 else 0)
        if novo_dado is not None:
            total += novo_dado
            qtde += 1

gen = media_movel()
next(gen)
valor = input('Digite um valor (ou FIM para encerrar): ')

while valor.upper() != 'FIM':
    resultado = gen.send(float(valor))
    print(f'\nMédia Móvel atual = {resultado:.3f}\n')
    valor = input('Digite um valor (ou FIM para encerrar): ')

print(f'Valor final da Média Móvel = {resultado:.3f}')

print('\nFim do programa\n')