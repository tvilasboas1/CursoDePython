""" Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

ex:
Digite um numero: 1834

unidade 4: 
dezena: 3
centena: 8
milhar: 1"""

num = int( input('Informe um Numero: '))

u = num //1 % 10 # 2 barras na divisão para ela ser arredondada == 1234 / 1 = 1234. Ai o resto divide por 10 ou seja 1234 / 10 = 123.4 resto = 4
d = num //10 % 10 #em 1234 = 1234 / 10 = 123.4 == so conta divisao inteira 123 /10 = 12.3 resto = 3
c = num //100 % 10
m = num //1000 % 10 #em 1234 / 1000 = 1.2 == 1.2 / 10 = 1 resto = 1

print('Analisando o Numero: {}'.format((num)))
print('UNIDADE: {}'.format(u))
print('DEZENA: {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR: {}'.format(m))

