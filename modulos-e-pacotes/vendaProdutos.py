def valor_venda(codigo, val_custo): # Função CONTAINER
    
    def altera_margem(): # Função CONTIDA no CONTAINER
        nonlocal margem # margem não é LOCAL dessa função
        if codigo[0] == '8':
            margem = 12/100
        elif codigo[0] == '9':
            margem = 10/100
    
    margem = 16/100
    altera_margem()
    val_venda = val_custo * (1 + margem)
    return val_venda



PcCusto = 100
CodProd = '1280'
PcVenda = valor_venda(CodProd, PcCusto)

print(f'\nProduto {CodProd}: compra = {PcCusto:.2f} e venda = {PcVenda:.2f}\n')

PcCusto = 100
CodProd = '8280'
PcVenda = valor_venda(CodProd, PcCusto)

print(f'\nProduto {CodProd}: compra = {PcCusto:.2f} e venda = {PcVenda:.2f}\n')

PcCusto = 100
CodProd = '9280'
PcVenda = valor_venda(CodProd, PcCusto)

print(f'\nProduto {CodProd}: compra = {PcCusto:.2f} e venda = {PcVenda:.2f}\n')