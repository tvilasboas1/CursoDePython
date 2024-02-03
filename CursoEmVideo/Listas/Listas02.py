valores =  []
valores.append(5)
valores.append(9)
valores.append(4)

for c in valores:
    print(c, end='')
print('\n')
for c, v in enumerate(valores): #Jeito diferente e bem util de fazer
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')