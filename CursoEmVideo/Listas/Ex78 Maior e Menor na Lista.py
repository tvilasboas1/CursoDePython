"""" Faça um programa que leia 5 valores numericos e guarde-os em uma lista.

 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """

# foi sugerido fazer com For in Range:

listanum = []
for c in range (0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c} : ' ))) # C + 1 evita que o contador comece contando de zero
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print('=-' * 30)

print(f'Voce digitou os valores {listanum}')
print(f'O MAIOR valor digitado: {maior} na posição:  ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')

print('')
print(f'O MENOR valor digitado: {menor} na posição: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}..', end='')


