lanche = ('Pão de Queijo', 'Pizza', 'Hamburger', 'Suco') # não precisa do Parentese, colocando apenas para efeito didatico
#Tuplas são imutaveis, ou seja não estao dispostas a mudar, ou seja não tem como mudar apos atribuir valor a variavel.
print(lanche)
print(f'Quando coloca [1:] {lanche[1:]}')
print(f'Quando coloca [2:5]{lanche[2:5]}')
print(f'Quando coloca [-1:1{lanche[-1:1]}')

print('{:^30}'.format('OutroMetodo'))
d = 19
for comida in lanche:
    d = d + 1
    print(f'Hoje dia {d} vamos comer: {comida}')

print('{:^30}'.format('OutroMetodo'))

for cont in range(0, len(lanche)):
    print(cont)

print('{:^30}'.format('OutroMetodo'))
for cont in range(0, len(lanche)):
    print(f'Hoje vamos comer: {lanche[cont]}')

print('{:^30}'.format('OutroMetodo'))
for cont in range(0, len(lanche)):
    print(f'Hoje vamos comer: {lanche[cont]} na posiçao {cont}')

print('{:^30}'.format('OutroMetodo'))
for pos, comida in enumerate(lanche):
    print(f'Hoje vamos comer: {comida} na posição {pos}')