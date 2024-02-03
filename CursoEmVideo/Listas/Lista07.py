galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # não esquecer de copiar
    dado.clear() # vai limpar os dados, mas eles já foram copiados para a lista 'Galera'
    # se não limpar a lista dado o sistema vai imprimir tudo 2x e vai virar uma bagunça
print(f'Lista Galera: {galera} ')
maiorIdade = menorIdade = 0
for p in galera:
    print(f'Nome: {p[0]} Idade: {p[1]}')
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maiorIdade = maiorIdade + 1
        #maiorIdade +=1
    else:
        print(f'{p[0]} é menor de idade.')
        menorIdade +=1 # fiz pela primeira vez mas gosto do outro metodo
print(f'\nA Galera é após o for in p c/ if and else: {galera}\nMaiores de Idade {maiorIdade}\nMenores de Idade {menorIdade}')