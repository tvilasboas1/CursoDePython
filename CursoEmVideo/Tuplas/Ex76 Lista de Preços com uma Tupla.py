'''' Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia.
No final mostre uma listagem de preços, organizando os dados em forma tabular. '''

# listagem  = (pão, 1.50, leite, 3.50, frango, 6.90) etc e por ai vai...

listagem = ('Lapis' , 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS" :^40}')
print('_' * 40)
for pos in range (0, len(listagem)): # vai ate a ultima posição da lista
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end= '')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('_'*40)