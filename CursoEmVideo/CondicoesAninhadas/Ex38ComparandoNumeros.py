""""Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais"""

num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))

if num1 > num2:
    print('O primeiro numero digitado {} é maior'.format(num1)) # so imbromando, nem precisava
elif num2 > num1:
    print('O segundo numero digitado {} é maior'.format(num2))
elif num1 == num2:
    print('Os dois  numero digitados {} e {} são iguais. '.format(num1, num2))