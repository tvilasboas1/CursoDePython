'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um DICIONARIO.
No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.'''


import time
from random import randint
from operator import itemgetter #Função itemgetter vai ser para colocar em sorted apenas o randint dentro do dicionario.

dados = { 'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
ranking = [] #optei em mudar para listas, pois pode ficar mais facil, e a lista recebe o dicionario.
print('----VALORES SORTEADOS----')
for k, v in dados.items():
    print(f'{k} tirou {v} no Dado' )
    time.sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True) #Reverse vai colocar o Sorted do Maior para o Menor. Key vai fazer colocar em ordem apenas o bloco (1)

print('-'*20)

for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]}' )
    time.sleep(1)