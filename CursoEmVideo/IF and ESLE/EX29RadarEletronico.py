""" ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO, SE ELE ULTRAPASSAR 80KM/H
MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO
A MULTA VAI CUSTAR 7.00 PARA CADA KM EXCEDIDO """

import random

velocidade = random.randint(60,99) #Randint faz um sorteio entre os numeros
print('O veiculo trafegou no radar na velocidade: {} KM/H'.format(velocidade))

if velocidade > 80:
    print('Voce foi multado, sua velocidade: {}KM/H é tera multa no valor R${} por KM excedente'.format(velocidade, (velocidade - 80 ) * 7))
else:
    print('Dentro dos limites de velocidade')
