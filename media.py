nome = str(input("\nDigite o nome do aluno: "))
idade = int(input("\nDigite a idade do aluno: "))
provas = int(input("\nDigite a quantidade de trabalhos avaliativos que o aluno fez: "))
i = 0
notas = []

while i < provas:
    nota = float(input("\nDigite as notas do aluno: "))
    notas.append(nota)
    i += 1

qtde_notas = len(notas)

def calculaMedia(notasDoAluno):
    soma = sum(notasDoAluno)  # Somando as notas diretamente
    media = soma / qtde_notas
    return media

def mostrarSituacao(nome, idade, media):
    if media >= 5 and media < 7:
        situacao = "recuperação"
    elif media >= 7:
        situacao = "aprovado"
    else:
        situacao = "reprovado"
    print(f"\nO aluno {nome} que possui {idade} anos teve média {media}, por isso sua situação é {situacao}")

# Calcular a média
media = calculaMedia(notas)

# Mostrar a situação
mostrarSituacao(nome, idade, media)
