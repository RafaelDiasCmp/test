from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2025-02-12 10:20'
mascara_ptbr = '%d/%m/%Y %a'
mascara_en = '%Y-%m-%d %H:%M'

# Corrigindo a impressão da data atual com a máscara correta
print(data_hora_atual.strftime(mascara_ptbr))

# Convertendo a string para datetime antes de formatar
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(type(data_convertida))

# Formatação da data convertida para uma string no formato desejado
data_convertida_str = data_convertida.strftime(mascara_en)
print(data_convertida_str)

print(type(data_convertida_str))
