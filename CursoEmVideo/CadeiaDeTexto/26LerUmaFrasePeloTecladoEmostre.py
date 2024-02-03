"""Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A"

Em que posição ela aparece a primeira vez.

Em que posição ela aparece a ultima vez."""

n = str(input('Informe a Frase p/ Leitura: ')).lstrip().upper()
print('QUANTAS VEZES APARECE A LETRA: "A"--> {}'.format(n.count('A')))
print('a letra "A" aparece pela primeira vez na posiição {} da String'.format(n.find('A')+1)) #Somar +1 vai fazer a String pular uma posição na palavra.
print('a letra "A" aparece pela ultima vez na posição {} da String'.format(n.rfind('A') +1))#Somar +1 aqui também é necessario pois a String sempre começa na posição Zero.

""" Uma observação interessante é a viagem na maionese em que se pode fazer com esta linguagem, poder somar casas em String e td mais é uma evoluçao. Cabe a um bom treino"""