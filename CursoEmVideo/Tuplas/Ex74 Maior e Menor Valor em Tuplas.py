''' Crie um programa que vai gerar 5 numeros aleatorios e coloca-lo em uma Tupla. Depois disso, mostre a listagem de numeros
gerados e também indique o menor e o maior valor que estão na tupla. '''
# Os valores sorteados foram
# O maior valor sorteado foi
# O menor valor sorteado foi

from random import randint
numeros = (randint(0,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram:  ', end='')
for n in numeros:
    print(f'{n} ', end=' ')
print(f'\nO Maior valor sorteado foi: {max(numeros)}')
print(f'O Menor valor sorteado foi: {min(numeros)}')