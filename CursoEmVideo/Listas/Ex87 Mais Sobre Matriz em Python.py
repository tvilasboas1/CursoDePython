""" Aprimore o Ex86:

a) A soma de todos os valores PARES digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.

exemplo =>

[7] [3] [2]
[6] [4] [9]
[1] [5] [3]

a soma dos valores pares = 12
a soma dos valores da terceira coluna = 14
o maior valor da segunda linha = 9"""
pares = somacoluna = maior = 0
matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
for l in range (0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('--' * 20)
for l in range (0, 3):
    for c in range (0, 3):
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]
        print(f'[{matriz[l][c]:^5}]', end= '')
    print()
print('--' * 20)
print(f'Soma dos Pares - > {pares}')
for l in range(0, 3):
    somacoluna = somacoluna + matriz[l][2]
print(f'Soma da 3° Coluna -> {somacoluna}')
for c in range (0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior n° da seg coluna -> {maior}')