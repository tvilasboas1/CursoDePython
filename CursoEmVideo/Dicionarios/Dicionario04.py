estado = {} #Dicionarios
brasil = [] #lista

for c in range (0, 3):
    estado['Nome'] = str(input('Nome do Estado:  '))
    estado['UF'] = str(input('Unidade Federativa: '))
    brasil.append(estado.copy()) #tem que usar o Copy nestes casos pois senão vira uma bagunça.

print(brasil)
print('--' * 15)
for c in brasil:
    for k, v in c.items(): #vai listar todos itens dentro da variavel brasil
        print(f' Campo K=  {k} Campo V=  {v} ') #no laço do laço sempre vem em ordem cronologica.

print()
print('--' * 15)
for c in brasil:
    for v in c.values():
        print(f'v de values {v}', end=' ') # para manter em linha reta. kkk
