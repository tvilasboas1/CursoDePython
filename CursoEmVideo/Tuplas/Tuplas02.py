#Colocando em ordem....
lanche = ('Pão de Queijo', 'Pizza', 'Hamburger', 'Suco')
print(lanche)
print(sorted(lanche)) #Sorted colocou em ordem alfabetica
print('{:^30}'.format('OutroMetodo'))
a = 1, 4, 3, 7, 5
b = 0, 2, 9, 11, 10
c = a + b
print(a)
print(b)
print(c)
print(sorted(c))
print('{:^30}'.format('OutroMetodo'))
print(len(f'{c} elementos')) # mostrando tamanho da tupla com 40
print(len(c)) #vai mostrar o tamanho da tupla
print(c.count(2)) # vai mostrar quantas vezes apareceu o numero 2.
print(c.index(11)) # vai mostrar em qual posição esta o numero 11.
print(c.index(9, 2)) # vai procurar um nove a partir da posição 2. Chama-se de Deslocamento.