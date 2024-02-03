""""Crie um programa que faça o computador jogar JokenPo com voce"""

import random


print("""VAMOS JOGAR JOKENPO.
USE O TECLADO PARA INFORMAR SUA JOGADA:
[1] = PEDRA
[2] = PAPEL 
[3] = TESOURA
""")

jog = int(input('Informe a sua jogada: '))
lista = [1,2,3]
pc = random.choice(lista)
print('THIAGO Escolheu a jogada: {}\nPC escolheu a jogada: {}'.format(jog, pc))

if jog ==1 and pc == 3 or jog ==2 and pc == 1 or jog == 3 and pc ==2:
    print('Thiago Venceu')
elif jog ==1 and pc ==1 or jog ==2 and pc == 2 or jog == 3 and pc ==3:
    print('Thiago empatou com PC, jogar novamente. ')
elif pc == 1 and jog ==3 or pc == 2 and jog ==1 or pc == 3 and jog ==2:
    print('Computador Venceu')
