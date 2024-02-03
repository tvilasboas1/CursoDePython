"""CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE SE ELE É PAR OU IMPAR """
num = int (input('Informe um numero: '))
resultado = num % 2

print('O numero informado = {}'.format(num))

if resultado == 0:
    print('O numero {} é par'.format(resultado))
else:
    print('O numero {} é Impar'.format(resultado))

# deixei aparecer o resto da divisão de proposito para entendimento futuro.

# so da para entender se colocar para rodar.
