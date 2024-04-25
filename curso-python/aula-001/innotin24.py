#  Operadores in enot in
#  Strings são interáveis
#  0 1 2 3 4 5
#  A l l y s o 
# -6-5-4-3-2-1

# nome = 'Allyson'
# print (nome[6])

# #OU

# print (nome[-1])

# # Ou checar por letra ou nome

# print ('n' in nome)
# print ('son' in nome)

nome = input('Digite o texto: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')
