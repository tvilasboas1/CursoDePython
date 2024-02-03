from random import randint
from time import sleep # Essa função é para fazer o Print ficar mais lento

computador = randint(0,5)  # Faz o computador escolher aleatoriamente um inteiro entre 0 e 5
print ('-=-' * 20)
print('VOU PENSAR EM UM NUMERO ENTRE 0 E 5. TENTE ADIVINHAR...')
print('_' *60)
jogador = int(input('Em qual numero eu pensei: '))
print('PROCESSANDO...')
sleep(2) # aqui no caso 2 segundos...

if jogador == computador:
    print('Parabens voce acertou!!!')
else:
    print('Eu errei, pensei no {} ao inves {}. Deu ruim'.format(computador, jogador))