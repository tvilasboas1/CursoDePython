"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

Ate 9 anos: MIRIM
Ate 14 anos: Infantil
Ate 19 anos: Junior
Ate 20 anos: Senior
Acima:  MASTER"""

import datetime # eu gosto mais assim, importanto a biblioteca inteira

anoatual = datetime.date.today().year
nasc = int(input('Informe o ano de Nascimento: '))

idade = anoatual - nasc
print('Idade: {} anos'.format(idade))

if idade < 9:
    print('Atleta Mirin')
elif 10> idade <= 14: # forçando o metodo matematico onde eu mais gostei.
    print('Atleta Infantil')
elif idade > 15 and  idade <= 19: # Forma classica
    print('Alteta Junior')
elif idade <=20:
    print('Atleta Senior')
else:
    print('Atleta Master')

""" Usando a matematica podemos economizar no if e elif, mas pode fazer do jeito classico também"""