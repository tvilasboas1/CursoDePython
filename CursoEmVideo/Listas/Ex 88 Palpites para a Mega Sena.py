"""" Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES. O programa vai perguntar quantos jogos serao gerados
e vai sortear 6 NUMEROS entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

Exemplos -> se quiser usar o time fica legal

Quantos jogos vc quer que eu sorteie?   4
Jogo 1: 4,8,10,20,26,38
Jogo 2: 14,20,23,35,38,47
Jogo 3: 2,11,15,24,43,48
Jogo 4: 6,26,28,29,30,46

Boa sorte

Em ordem de maior para menor"""

from time import sleep
from random import randint
print('--' * 16)
print('SIMULADOR DE JOGOS DA MEGA-SENA')
print('--' * 16)
lista = list()
jogos = list()
tot = 1

jog = int(input('N° de Simulaçõoes: '))
while tot <= jog:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1
print(f'----SORTEANDO {jog} JOGOS---')

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}:  {l}')
    sleep(1)

print('--' * 16)
print('BOA SORTE')