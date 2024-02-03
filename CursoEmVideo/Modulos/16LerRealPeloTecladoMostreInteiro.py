#CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA

'''import math
num = float(input('Digite um valor: '))
print('O valor digitado é: {} sua porção inteira é: {}'.format(num, math.trunc(num))) ##Esse truncar faz o numero quebrado ficar inteiro.'''


# EXISTE DUAS FORMAS DE SEREM FEITOS

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado = {} e seu valor inteiro é = {}'.format(num, trunc(num)))

