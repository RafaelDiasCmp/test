def ler_arquivo(nome_arq):
    for uma_linha in open(nome_arq, 'r'):
        uma_linha = uma_linha.split(';')
        yield uma_linha[0], int(uma_linha[3])
        
        #yield uma_linha.rstrip() remove pulo de linha

arquivo = input('Digite o nome do arquivo: ')

for linha in ler_arquivo(arquivo):
    print(linha)