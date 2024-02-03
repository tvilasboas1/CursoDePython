"""" Crie um programa que crie uma Matriz de dimensaão 3x3 e preencha com valores lidos pelo teclado.

No final mostre na tela com a formatação correta

tem que manjar esse 86 para fazer o 87"""

num = [[], [], []]
matriz = 0
for c in range (0, 3):
    matriz = int(input(f'Digite um Valor para [0, {c}]: '))
    num[0].append(matriz)

for c in range(0, 3):
    matriz = int(input(f'Digite um Valor para [1, {c}]: '))
    num[1].append(matriz)

for c in range (0, 3):
    matriz = int(input(f'Digite um Valor para [2, {c}]: '))
    num[2].append(matriz)
print(f'Imprimindo toda a Matriz: {num}')
print('---' * 25)
print(f'M1 -> {num[0]}')
print(f'M2 -> {num[1]}')
print(f'M3 -> {num[2]}')
