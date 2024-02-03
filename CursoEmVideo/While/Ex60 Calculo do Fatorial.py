"""  Faça um programa que leia um numero qualquer e mostre o seu Fatorial.

 Fazer com While e tambem For"""

print('Vamos apresentar o Fatorial do numero.')
num = int(input('Qual o numero a ser calculado ? '))
print('Vamos calcular {}! '.format(num) )
cont = num
fat = 1
while cont > 0:
    print('{}'.format(cont), end= '')
    print(' x ' if cont > 1 else ' = ', end= '') #Este If e Else encaixa perfeito nesse caso
    fat = fat * cont
    cont = cont - 1
print(' {}'.format(fat))
