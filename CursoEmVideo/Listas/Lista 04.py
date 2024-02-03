# outras formas...
a  = [2, 3, 4, 7]
b = a
b[2] = 8 # aqui o B recebe 8. Mas como a lista esta ligada com A, o A também recebe 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# aqui vemos que um recebendo o outro acaba ligando as listas.
print('-' * 30)
a  = [2, 3, 4, 7]
b = a[:] # aqui B recebeu uma Copia de A, porém sem ligar, ou seja, podem ser feitas alterações em B
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# só imprimir para ver a diferença