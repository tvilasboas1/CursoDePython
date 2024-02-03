""" DESENVOLVA um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem PARES Se o valor digitado
 for IMPAR, desconsidere-o"""
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Informe um numero: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Acabou, informado {} Pares, a soma dos numeros pares é = {}.'.format(cont, soma))