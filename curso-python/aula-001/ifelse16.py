# if / elif / else
# se / se não se / se não
""""
# Exercício 1

entrada = input ('Você quer "entrar" ou "sair"? ')



if entrada == 'entrar':
    print('Você entrou no sistema')

elif entrada == 'sair' :
    print('Você saiu do sistema')

else:
    print('Você não digitou nem entrar e nem sair')



"""
"""

# Exercício 2

idade = int(input ('Informe sua idade: '))


if idade < 18:
    print('Você é menor de idade')

elif idade >= 18 and idade < 65:
    print('Você é um adulto')

else:
    print('Você é um idoso')
    print(' ')


"""


# Exercício 3

numero = int(input('Digite um número:'))

if numero > 0:
    print ('Número positivo')

elif numero < 0:
    print ('Número negativo')

else:
    print ('Número zero')