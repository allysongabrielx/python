"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# try:
#     numero = int(input ('Digite um número inteiro: '))

#     if numero % 2 == 0:
#         print(f'O número {numero} é PAR')
#     else:
#         print(f'O número {numero} é IMPAR')
# except ValueError:
#     print('Isso não é um número inteiro.')


"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario = float(input('Digite a hora: '))

# if horario >= 0 and horario < 12:
#     print ('Bom dia!')
# elif horario >= 12 and horario < 18:
#     print ('Boa tarde!')
# elif horario >= 18 and horario <= 23:
#     print ('Boa noite!')
# else:
#     print('Horario invalido')
    

"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""
primeiro_nome = input ('DIgite seu primeiro nome: ')

if len (primeiro_nome) > 1 and len(primeiro_nome)<= 4:
    print('Seu nome é curto.')
elif len (primeiro_nome) >= 5 and len(primeiro_nome) <= 6:
    print('Seu nome é médio.')
elif len (primeiro_nome) > 6:
    print('Seu nome é grande.')
else:
    print('Digite mais de uma letra.')
