num = [[], [], []]
matriz = pares = somacoluna = 0

for c in range (0, 3):
    matriz = int(input(f'Digite um Valor para [0, {c}]: '))
    if matriz % 2 == 0:
        pares = pares + matriz
    num[0].append(matriz)
    somacoluna = somacoluna + c[2]
for c in range(0, 3):
    matriz = int(input(f'Digite um Valor para [1, {c}]: '))
    if matriz % 2 == 0:
        pares = pares + matriz
    num[1].append(matriz)

for c in range (0, 3):
    matriz = int(input(f'Digite um Valor para [2, {c}]: '))
    if matriz % 2 == 0:
        pares = pares + matriz
    num[2].append(matriz)

print(f'Imprimindo toda a Matriz: {num}')
print('---' * 10)
print(f'M1 -> {num[0]}')
print(f'M2 -> {num[1]}')
print(f'M3 -> {num[2]}')
print('---' * 10)
print(f'A soma dos Pares ->>> {pares}')
