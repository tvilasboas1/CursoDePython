
jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas Partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos Gols na Partida ->> {c + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('DESEJA CONTINUAR ? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite Novamente...')
    if resp == 'N':
        break
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='') # 3 caracteres alinhado a direita
    for d in v.values():
        print(f'{str(d):<15}', end='') #15 caracteres alinhados a direita
    print()
print('-=' * 40)




"""print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'---> Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols. ')"""


