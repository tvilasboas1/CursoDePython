""" Crie um programa onde o usuario possa digitar SETE VALORES NUMERICOS e cadastreos em uma LISTA UNICA que mantenha separados
os valores PARES e IMPARES. No final, mostre os valores pares e impares em ordem CRESCENTE.

Exemplo => usar for in range

as duas listas tem que estar dentro de uma lista
1 lista composta com 2 listas internas
"""
num = [[], []] # lista dentro da lista. Para fazer uma lista par e uma lista impar
valor = 0

for c in range(1,8):
    valor = int(input(f'Informe o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)# observar esse num na posição 0:
    else:
        num[1].append(valor)# observar esse num na posição 1:
print('--' * 30)
print(f'Valores Gerais -> {num} ')
print('--' * 30)
print(f'Lista de Pares ->> {num[0]}')
print(f'Lista de Impares ->> {num[1]}')