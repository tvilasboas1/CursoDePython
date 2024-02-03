#Poderia ser  from random import shufle ( para economizar memoria do Notebook )

import random



n1 = str(input('Informe o nome do primeiro aluno: '))
n2 = str(input('Informe o nome do segundo aluno: '))
n3 = str(input('Informe o nome do terceiro aluno: '))
n4 = str (input('Informe o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista) #shufle serve para embaralhar
print('A ordem de apresentação sera: ')
print(lista)
