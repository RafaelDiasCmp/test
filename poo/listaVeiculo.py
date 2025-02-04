from pacote.classeVeiculo import Veiculo


LstV = []

for s in open("C:\\Users\\raffa\\OneDrive\\Desktop\\teste\\yield\\veiculos.txt", 'r'):

    s = s.split(';') #critério de separação

    v = Veiculo(s[0], s[1], int(s[2]), int(s[3])) # Objeto veículo com os parâmetros lidos da placa - modelo - ano - km
    LstV.append(v)

for v in LstV:
    v.exibe()

print('\nFim do programa\n')