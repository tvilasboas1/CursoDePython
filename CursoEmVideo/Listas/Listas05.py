dados = list()
dados.append('Pedro')
dados.append(21)
dados.append(1.80)
print(dados)
print(f'Ou {dados[1]} que vai imprimir apenas o bloco 1 da lista. ')
dados2 = list()
dados2.append('Thiago')
dados2.append('34')
dados2.append('1.70')
dados3 = list()
dados3.append('João')
dados3.append('41')
dados3.append(1.85)


pessoas = list()
pessoas.append(dados[:])# Quando vc coloca : automaticamente imprime tudo, ou pode colcar o numero do bloco a imprimir..
pessoas.append(dados2[:])
pessoas.append(dados3[:])
print(f'\nAqui imprimindo a lista dentro da lista: {pessoas}')

"""" Ou pode ser também: 
 pessoas = [['Pedro', 21, 1.8], ['Thiago', '34', '1.70'], ['Pedro', 21, 1.8]]"""
print(f'Pegar Pessoas no Bloco 1 Posição 0:  {pessoas[1][0]}') # aqui ele pega as pessoas no bloco 1 e na posição zero é imprime.
print(f'Pegar Pessoas no Bloco 2 Posição 1:  {pessoas[2][1]}')
print(f'Pegar Pessoas no Bloco 0 Posição 1:  {pessoas[0][1]}')
print('Pegar simplesmente tudo de Pessoas: {}'.format(pessoas[1]))# Fiz com o Format só para zoar