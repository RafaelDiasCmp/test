import sqlite3
conector = sqlite3.connect('C:/Users/raffa/OneDrive/Desktop/teste/loja.db')
cursor = conector.cursor()
sql = "delete from produto where codigo = ?"
excluidos = []
codigo = input('Digite o código a ser excluído: ')

while codigo.upper() != 'FIM':
    cursor.execute(sql, [int(codigo)])
    excluidos.append(int(codigo))
    codigo = input('Digite o código a ser excluído: ')
conector.commit()