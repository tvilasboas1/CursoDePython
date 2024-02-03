from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)

print(''' Opções de Jogada:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jog = int(input('Informe a sua jogada: '))
print('THIAGO JOGOU: {}'.format(itens[jog]))
print('COMPUTADOR JOGOU: {}'.format(itens[pc]))

if pc == 0:
    if jog ==0:
        print('EMPATE')
    elif jog ==1:
        print('JOGADOR VENCE')
    elif jog == 3:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Invalida')
elif pc == 1:
    if jog == 0:
        print('COMPUTADOR VENCE')
    elif jog == 1:
        print('EMPATE')
    elif jog == 3:
        print('JOGADOR VENCE')
    else:
        print('Jogada Invalida')
elif pc == 2:
    if jog == 0:
        print('JOGADOR VENCE')
    elif jog == 1:
        print('COMPUTADOR VENCE')
    elif jog == 2:
        print('EMPATE')
    else:
        print('Jogada Invalida')