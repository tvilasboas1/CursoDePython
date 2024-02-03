"""ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NUMERO ENTRE 0 E 5
E PEÇA PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NUMERO APRESENTADO PELO COMPUTADOR
O PROGRAMA DEVERA ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU"""

import random

user = int (input('Escolha um Numero entre 1 e 5: '))
lista = [0,1,2,3,4,5] # não tem necessidades de declarar uma variavel =D { Descobri sozinho }
escolhido = random.choice(lista)
print('O numero sorteado foi: {} '.format(escolhido))

print('Voce Digitou {} é o sistema escolheu {} '.format(user,escolhido))
if user == escolhido:
    print('PARABENS VOCÊ VENCEU')
else:
    print('Droga, vc perdeu kkk')

