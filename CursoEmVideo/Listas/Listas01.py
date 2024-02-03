"""" Listas ficam entre colchetes [] diferente de Tuplas() que ficam entrem parenteses..."""

num = [2, 5, 9, 1, 4, 9, 21, 6]
num[2] = 3
num.append(7) # aqui inclui o numero 7 na lista.
#num.sort() # aqui coloca em ordem alfabetica
#num.sort(reverse=True) # coloca em ordem de Z ate A. Ou seja de trás para frente
num.insert(2, 0) # neste caso vamos inserir o numero 0 na posição 2.
print(num)
print(f'Essa lista tem o total de {len(num)} elementos.')
num.pop() # aqui remove automaticamente o ultimo elemento da lista
num.pop(3) # aqui vai remover automaticamente o elemento na posição 3 ou da lista ou qualquer um listado
print(f'Testando apos as remoções \n{num} deu ok ')
if 5 in num:
    num.remove(5) # aqui vamos remover o numero 5, se e somente se ele estiver na lista
else:
    print('Numero não encontrado...')
if 99 in num:
    num.remove(99)
else:
    print('Numero 99 não encontrado na lista')
print(f'Testando o NUM após as novas remoçoes de if e else: {num}')