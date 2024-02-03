""" Faça um programa que leia um numero INTEIRO e diga se ele é ou não um NUMERO PRIMO.  """

num = int(input('Informe um numero: '))
tot = 0
for c in range(1,num + 1):
    if num % c == 0:
        tot = tot + 1
    else:
        print(c)
print('O numero {} foi Divisivel {} vezes'.format(num, tot))
if tot ==2:
    print('E por isso ele é primo')
else:
    print('É por isso ele NÃO É PRIMO')