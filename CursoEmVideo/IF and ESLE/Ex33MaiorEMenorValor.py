"""Faça um programa que leia 3 Numeros e Mostre qual é o maior e o menor entre os 3 """

num1 = int (input ('Informe um valor: '))
num2 = int (input ('Informe um valor: '))
num3 = int (input ('Informe um valor: '))

if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
