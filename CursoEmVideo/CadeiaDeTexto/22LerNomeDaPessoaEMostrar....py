"""CRIE um programa que leia o nome completo da pessoa e mostre:
Quantas letras sem considerar espaços
O nome com todas as letras maiusculas
O nome com todas minusculas
Quantas Letras tem o primeiro Nome"""


nome = str (input(' Informe o nome completo do cliente: ')).strip() #sim pode usar a função Strip aqui para eliminar os espaços.
print('')
print('Nome completo em MAISCULAS: {}.'.format(nome.upper()))
print('Nome completo em MINUSCULAS: {}'.format(nome.lower()))
print('Nome possui {} LETRAS'.format(len(nome) - nome.count(' '))) #o count vai eliminar os espaços na contagem das letras, por isso a subtração
#print('Seu primeiro nome possui {} LETRAS'.format(nome.find(' '))) #nao entendi o porque destas aspas simples, depois eu descubro
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0]))) #mais facil entender






