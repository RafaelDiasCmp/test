from datetime import datetime, timedelta, date

# P, M, G
tipo_carro = input('Digite o tipo do carro: ')
tempo_pequeno = 130
tempo_medio = 45
tempo_grande = 160
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou {data_atual} e ficará pronto às {data_estimada}')

elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou {data_atual} e ficará pronto às {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou {data_atual} e ficará pronto às {data_estimada}')

print(date.today() - timedelta(days=1))

resultado = datetime(2025, 2, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())