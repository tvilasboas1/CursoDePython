"""" Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999
que é a CONDIÇÃO DE PARADA. No final mostre QUANTOS NUMEROS foram digitados e qual foi a SOMA entre eles
(desconsiderando o flag) ou seja o nº 999 """
num = 0
cont = 0
somador = 0

while num != 999:
    num = int(input('Leia um numero: Press 999 to STOP: '))
    if num !=999:
        somador = somador + num
    else:
        cont = cont - 1
    cont = cont + 1
print('\nForam digitados {} Numeros.\nA soma entre eles é: {}'.format(cont, somador))