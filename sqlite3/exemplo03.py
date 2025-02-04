import sqlite3
conector = sqlite3.connect('C:/Users/raffa/OneDrive/Desktop/teste/loja.db')
cursor = conector.cursor()
sql = "select * from produto"
cursor.execute(sql)
dados = cursor.fetchall()
cursor.close()
conector.close()

print('\nConsulta ao Banco de Dados "loja.db" \n')
print('Dados da tabela "produto"')
print("-" * 61)
print("{:7}{:40}{:>8}{:>6}".format('Código', 'Descrição', 'Preço', 'Estq'))
print("- " * 31)

for d in dados:
    print("{:<7}{:40}{:8.2f}{:6}".format(d[0], d[1], d[2], d[3]))
    print("-" * 61)
    print("Encontrados {} registros".format(len(dados)))
print("\n\nFim do programa")
