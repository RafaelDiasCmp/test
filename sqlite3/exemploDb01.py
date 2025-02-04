import sqlite3

conector = sqlite3.connect('loja.db')
cursor = conector.cursor()

sql = """
    create table produto
    (codigo integer, descr text, preco numeric, qtdestq integer)
"""

cursor.execute(sql)

sql = """
    insert into produto (codigo, descr, preco, qtdestq)
    values(1138, 'lápis preto', 1.90, 375)
"""
cursor.execute(sql)

sql = """
    insert into produto (codigo, descr, preco, qtdestq)
    values(1150, 'caderno preto', 10.90, 230)
"""
cursor.execute(sql)
conector.commit()

cursor.close()
conector.close()

print('\nFim dor programa\n')
