""" Melhore o jogo do DESAFIO 28 onde o computador vai 'pensar' em um numero entre 0 e 10. Só que agora o jogador vai
 tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer."""


from random import randint
print('VAMOS TENTAR ADIVINHAR O NUMERO QUE O COMPUTADOR PENSOUU.')

computador = randint(0,10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite: '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('E um numero maior, tente novamente...')
    else:
        print('E um numero menor, tente novamente...')
print('Acertou apos {} PALPITES'.format(palpite))
