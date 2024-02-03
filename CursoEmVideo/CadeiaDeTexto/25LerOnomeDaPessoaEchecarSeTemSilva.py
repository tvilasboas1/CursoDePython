"""Crie um programa que leia o nome de uma pessoa é cheque se ela contem "SILVA" no nome"""



nome = str(input('NOME COMPLETO:  ')).lstrip()
print('é silva: {}'.format('silva' in nome.lower())) # AQUI INDEPENDENTE DA FORMA QUE EU ESCREVER VAI VIRAR TD MINUSCULO
print('É SILVA: {}'.format('SILVA' in nome.upper())) #AQUI INDEPENDENTE DA FORMA QUE EU ESCREVER VAI VIRAR TD MAIUSCULO

#Fiz das duas formas e deixei bem explicito para nunca mais esquecer