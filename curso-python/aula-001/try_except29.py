"""
Introdução ao try/except
try -> Tentar executar o código
Except -> Ocorreu algum erro ao tentar executar
"""

numero_1 = input('Primeiro número: ')
numero_2 = input('Segundo número: ')

try:

    numero_1 = float(numero_1)
    numero_2 = float(numero_2)

   
    soma = (numero_1 + numero_2)
    print(f'A soma de {numero_1} + {numero_2} é = {soma}')

    subtracao = (numero_1 - numero_2)
    print(f'A subtração de {numero_1} - {numero_2} é = {subtracao}')

    multiplicacao = (numero_1 * numero_2)
    print(f'A multiplicação de {numero_1} * {numero_2} = {multiplicacao}')

    divisao = (numero_1 / numero_2)
    print(f'A divisão de {numero_1} / {numero_2} = 1')

    
except:
    print('Isso não é um número')

