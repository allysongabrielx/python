# Calculando IMC:

nome = 'Allsyon Gabriel'
altura = 1.70
peso = 72
imc = peso / (altura * altura)

linha_2 = f'{imc:.2f}' # LInha de formatação servepara colocar casas decimais

print(nome, 'tem', altura, 'de altura', 'pesa:', peso, 'Kg', 'e seu IMC é:')
print(linha_2)


#resultados menores que 16 — magreza grave;
#resultados entre 16 e 16,9 — magreza moderada;
#resultados entre 17 e 18,5 — magreza leve;
#resultados entre 18,6 e 24,9 — peso ideal;
#resultados entre 25 e 29,9 — sobrepeso;
#resultados entre 30 e 34,9 — obesidade grau I;
#resultados entre 35 e 39,9 — obesidade grau II ou severa;
#resultados maiores do que 40 — obesidade grau III ou mórbida.
