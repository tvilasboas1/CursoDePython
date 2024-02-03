""" Aprimore o Desafio 093 para que ele funcione com varios jogadores, incluindo um sistema de visualizaçoes de detalhes do aproveitamento
de cada jogador. """

jogador = {}
gol = []
jog = []

while True:
   jogador['NOME:'] = str(input('Nome: '))
   jogador = int(input(f'N° de Partidas Jogadas de {jogador["NOME:"]}: '))
   print('-=' * 18)
   for c in range(0,partidas):
      gol.append(int(input(f'GOLS NA PARTIDA ->> {c + 1}: ')))
   jog.append(jogador['NOME:'])
   cont = str(input('DESEJA CONTINUAR ? [S/N]: ')).upper()[0]

   if cont == 'N':
      break



jogador['GOLS:'] = gol[:]
jogador['TOTAL DE GOLS:'] = sum(gol) #sum faz a lista somar os valores int dentro dela

print('-=' * 18)
print(jogador)

for k,v in jogador.items():
   print(f'O campo {k} tem o valor {v}')
print('-=' * 18)
print(f'O Jogador {jogador["NOME:"]} jogou {partidas} de PARTIDAS. ')

for i, v in enumerate(jogador['GOLS:']):
   print(f' ->> Na partida {i}, fez {v} gols.')
print('-=' * 18)
print(f'Foi um total de {jogador["TOTAL DE GOLS"]} GOLS ')