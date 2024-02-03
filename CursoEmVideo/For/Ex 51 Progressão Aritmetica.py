""" Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA.
No final, mostre os 10 primeiros termos dessa progressão"""

a1 = int(input('Digite a A1 (primeiro termo da PA): '))
r = int(input('Informe a Razãao: '))
decimo = a1 + (10 - 1) * r
for c in range(a1,decimo + r, r):
    print('{}'.format(c), end='-> ')

print('Deuuu')