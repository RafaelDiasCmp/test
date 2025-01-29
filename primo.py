def Primo(V):
    if not isinstance(V, int):
        raise TypeError('Tipo inválido, o argumento deve ser um inteiro')

    if V < 2:
        raise ValueError('Valor inválido, o argumento deve ser no mínimo 2')
    
    if V == 2:
        return True
    elif V % 2 == 0:
        return False
    else:
        raiz = pow(V, 0.5)
        i = 3
        while i <= raiz:
            if V % i == 0:
                return False
            i += 2
        return True

try:
    n = int(input('Digite um número inteiro: '))
    if Primo(n):
        print(f'O número {n} é Primo')
    else:
        print(f'O número {n} não é Primo')

except ValueError as ve:
    print(f'Erro! {ve}')
except TypeError as te:
    print(f'Erro! {te}')  
