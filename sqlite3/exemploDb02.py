import sqlite3

conector = sqlite3.connect('loja.db')
cursor = conector.cursor()


try:
    sql = "drop table produto"
    cursor.execute(sql)

except sqlite3.OperationalError:
    pass


sql = """
    create table produto
    (codigo integer, descr text, preco numeric, qtdestq integer)
"""

cursor.execute(sql)

sql = """
    insert into produto (codigo, descr, preco, qtdestq)
    values(?, ?, ?, ?)
"""

nome_arq = 'C:/Users/raffa/OneDrive/Desktop/teste/sqlite3/papelaria.txt'

for linha_arq in open(nome_arq, 'r'):
    dados = linha_arq.split(';')
    print(dados)
    cursor.execute(sql, dados)

conector.commit()

cursor.close()
conector.close()

print('\nFim dor programa\n')
