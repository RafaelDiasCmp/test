import sqlite3
conector = sqlite3.connect('C:/Users/raffa/OneDrive/Desktop/teste/loja.db')
cursor = conector.cursor()
sql = """
 update produto
 set custo = ?, aliqicms = ?, qtdemin = ?
 where codigo = ?
 """

nome_arq = 'C:/Users/raffa/OneDrive/Desktop/teste/sqlite3/papelaria.txt'
for linha_arq in open(nome_arq, encoding='utf-8'):
    dados = linha_arq.rstrip().split(';')
    dados.append(dados[0]) # coloca o código no final da lista
    del(dados[0]) # elimina o código do início da lista
    print(dados)
    cursor.execute(sql, dados)

conector.commit()

print('A tabela produto foi atualizada')

cursor.close()
conector.close()