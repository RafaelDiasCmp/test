def func(x):
    if x < 0:
        raise ArithmeticError
    return 2 * x

try:
    x = int(input('Digite um inteiro: '))
    print(f'func({x}) = {func(x)}')
except ArithmeticError:
    print('Erro 1')
except ValueError:
    print('Erro 2')
except Exception:
    print('Erro 3')