""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente ate ter um valor correto. """

# aqui vai dar enquanto o Sexo for M ou F
sexo = str(input('Informe o seu sexo [ M / F ] ')).strip().upper()[0]
while sexo == 'F' or sexo == 'M':
    sexo = str(input('Digite o Sexo: ')).strip().upper()[0] #Este Zero vai fazer o programa pegar apenas a primeira letra independente do que for digitado.
print('Fim')

# pode ser feito também. Aqui vai dar enquanto o Sexo nao for M ou F
""" 
while sexo not in  'MF': 
    sexo = str(input('Digite o Sexo: ')).strip().upper()[0]
"""