"""" Faça um programa que jogue PAR OU IMPAR com o Computador, o jogo só sera interrompido quando o jogador PERDER, mostrando o total
de vitorias consecutivas que ele conquistou no final do jogo."""
import random
valor = 0
while True:
        jog = int (input('Informe um Numero P/ Jogar Par ou Impar:  '))
        comp = random.randint(1,10)
        if jog == 0:
                break
        else:
                total = jog + comp
                tipo = ' '
                while tipo not in 'PI':
                        tipo = str(input('ESCOLHA -> PAR ou IMPAR: ')).lstrip().upper()[0]
                        if tipo == 'P':
                                if total % 2 == 0:
                                        print('PARABENS, venceu...')
                                        print(f'Jogador -> Jogou -> ({jog})\nComputador -> Jogou -> ({comp})\n--->: ({total})')
                                        valor = valor + 1
                                else:
                                        print('Deu ruim. Perdeu...')
                                        print(f'Jogador -> Jogou -> ({jog})\nComputador -> Jogou -> ({comp})\n--->: ({total})')
                        if tipo == 'I':
                                if total % 2 == 1:
                                        print('PARABENS. Venceu...')
                                        print(f'Jogador -> Jogou -> ({jog})\nComputador -> Jogou -> ({comp})\n--->: ({total})')
                                        valor = valor + 1
                                else:
                                        print('DEU RUIM ZÉ. PERDEU')
                                        print(f'Jogador -> Jogou -> ({jog})\nComputador -> Jogou -> ({comp})\n--->: ({total})')


print(f'GAME OVER\n-> you win {valor} times')

