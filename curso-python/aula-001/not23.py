#  Operador lógico "not"
#  Usando para inverter expressões
#  not True = False
#  not False = True

senha = input ('Senha: ')

if senha == '123456':
    print ('Entrou')

if not senha:
    print ('Você não digitou nada')

else:
    print ('Senha incorreta.')

