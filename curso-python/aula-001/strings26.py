'''
s - string
d e i - int
f -float
.<número de dígitos>f 
x e x - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >20}')
print(f'{variavel: <10}')
print(f'{variavel: ^20}')
print(f'{1000.487555161516:.2f}')
print(f'{variavel!r}')