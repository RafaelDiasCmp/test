import sqlite3
conector = sqlite3.connect('C:/Users/raffa/OneDrive/Desktop/teste/loja.db')
cursor = conector.cursor()

sql = """
    insert into produto (codigo, descr, preco, qtdestq)
    values (?, ?, ?, ?)
"""

print('Digite os dados separados por vírgulas')
print('Codigo,Descrição,Preço,Estoque')

Ler = input()

while Ler != '':
    D = Ler.split(',')
    try:
        cursor.execute(sql, D)
        conector.commit()
    except:
        print('{} Dados inválidos'.format(D))
    else:
        print(' '*30, '...dados inseridos com sucesso')
    finally:
        print('\nCodigo,Descrição,Preço,Estoque')
    Ler = input()