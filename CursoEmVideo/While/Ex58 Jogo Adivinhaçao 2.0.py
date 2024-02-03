""" Melhore o jogo do DESAFIO 28 onde o computador vai 'pensar' em um numero entre 0 e 10. Só que agora o jogador vai
 tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer."""

import random

#user = int(input('Escolha um Numero entre 1 e 10: '))
escolhido = random.randint(0, 10)
user = 0

while user != escolhido:
    user = int (input('Escolha um Numero entre 1 e 10: '))
    if user == escolhido:
        print('PARABENS VOCÊ VENCEU\nO numero sorteado foi {}'.format(escolhido))
    elif user > escolhido:
        print('Droga, vc perdeu.... Tente um numero MENOR kkk')
    else:
        print('Droga, vc perdeu.... Tente um numero MAIOR kkk'




