'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador de futebol e quantas partidas
ele jogou. Depois vai ler a quantidade de Gols feitos em cada partida. No final, tudo isso sera guardado em um dicionario, incluindo total de gols feitos
no campeonato.'''

jogador = {}
gol = []
jogador['NOME:'] = str(input('Nome: '))
partidas = int(input(f'N° de Partidas Jogadas de {jogador["NOME:"]}: '))
print('-=' * 18)
for c in range(0,partidas):
   gol.append(int(input(f'GOLS NA PARTIDA {c + 1}: ')))

jogador['GOLS: '] = gol[:]
jogador['TOTAL DE GOLS'] = sum(gol) #sum faz a lista somar os valores int dentro dela

print('-=' * 18)
print(jogador)

for k,v in jogador.items():
   print(f'O campo {k} tem o valor {v}')
print('-=' * 18)
print(f'O Jogador {jogador["NOME:"]} jogou {partidas} de PARTIDAS. ')

for i, v in enumerate(jogador['GOLS: ']):
   print(f' ->> Na partida {i}, fez {v} gols.')
print('-=' * 18)
print(f'Foi um total de {jogador["TOTAL DE GOLS"]} GOLS ')