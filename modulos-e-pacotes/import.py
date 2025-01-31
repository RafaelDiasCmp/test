#import sys
#sys.path.append("C:/Users/raffa/OneDrive/Desktop/teste/pacote")

import pacote.utils_bool as ub # apelido aos módulos
import pacote.utils_txt as ut 


print('-' * 20)
for s in dir(): # apelido inserido no namespace global
    if '__' not in s:
        print(s)
print('-' * 20)


a = 17
print(ub.texto)
r = ub.primo(a)
print(f'\n{a} é primo? {r}\n')

r = ub.paridade(a)
print(f'\n{a} é par? {r}\n')

print('-' * 20)

print(ut.texto)
ut.primo(a)
ut.paridade(a)

print('\nFim do programa\n')







