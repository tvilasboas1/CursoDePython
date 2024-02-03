""" Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artificio, indo de 10 ate 0,
com uma pausa de 1 segundo entre eles."""
print('='*20)
print('CONTAGEM REGRESSIVA')
print('='*20)
from time import sleep

for c in range(10,0,-1):
    print(c)
    sleep(1)

print('FELIZ ANO NOVO')

