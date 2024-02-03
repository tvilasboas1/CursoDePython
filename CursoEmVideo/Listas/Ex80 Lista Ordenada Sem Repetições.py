"""" Crie um programa onde o usuario possa digitar CINCO valores numericos e cadastre-os em uma LISTA, JÁ NA POSIÇÃO CORRETA de
 inserção (sem usar o sort()).

 No final, mostre a lista ordenada na tela. """

lista = []
for c in range (0,5):
    num = int(input('Digite um Numero: '))
    if c == 0 or num > lista[len(lista) - 1]:
        lista.append(num)
        print('Adicionado no Final da Lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f' Numero foi adicionado na Posição {pos} da lista...') # bom para checar e aprender
                break
            pos = pos + 1
print('=' * 30)
print(f'Os valores digitados em ordem foram {lista}')


