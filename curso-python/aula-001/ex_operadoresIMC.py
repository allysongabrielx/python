# Calculando IMC:

nome = input ('Digite seu nome: ')
altura = float(input('Digite sua altura (em metros): '))
peso = float(input('Digite seu peso (em quilogramas): '))

# Calculando o IMC
imc = peso / (altura ** 2)

# Exibindo o IMC em casa decimal:

linha_2 = f'{imc:.1f}' # LInha de formatação serve para colocar casas decimais

# Verificando o status com base no IMC:

if imc < 18.5:
    print('Magreza leve')

elif 18.5 <= imc < 25:
    print('Peso ideal')

else:
    print('Sobrepeso')

# Exibindo as informações pessoais:

print(f'{nome} tem {altura} de altura, pesa {peso} Kg, e seu IMC é {linha_2}.')





#resultados menores que 16 — magreza grave;
#resultados entre 16 e 16,9 — magreza moderada;
#resultados entre 17 e 18,5 — magreza leve;
#resultados entre 18,6 e 24,9 — peso ideal;
#resultados entre 25 e 29,9 — sobrepeso;
#resultados entre 30 e 34,9 — obesidade grau I;
#resultados entre 35 e 39,9 — obesidade grau II ou severa;
#resultados maiores do que 40 — obesidade grau III ou mórbida.
