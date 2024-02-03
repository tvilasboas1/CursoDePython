""" REFAÇA o Exercicio 009, mostrando a Tabuada de um numero que o usuario escolher, so que agora ultilizando o laço For."""

num = int(input('Digite um Numero: '))
print('VAMOS FAZER A TABOADA: \n')
m = 0  # multiplicação.

for c in range(0,11):
    m = c + num
    print(' {} + {} = {}'.format(num,c,m))
print('FIM SOM.')

for c in range(10,0,-1):
    m = c - num
    print(' {} - {} = {}'.format(num,c,m))
print('FIM SUB')

for c in range(0,11):
    m = c * num
    print(' {} X {} = {}'.format(num,c,m))
print('FIM MULT')

