
cont = ( 'zero', 'um', 'dois', 'tres', 'quatro,', 'cinco', 'seis',  'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'desessete ', 'dezoito', 'dezenove', 'vinte')

seguir = ''
tot = 0
recebe = 0
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num >= 0 and num <= 20:  # pode ser também -> if 0 <= num <= 20:
        tot = tot + 1
        print(f'Foi digitado o numero ->:  {cont[num]}')
    seguir = str(input('Deseja Continuar: (S / N) -> ')).lstrip().upper()[0]
    if seguir != 'S' and  seguir !='N':
        print('COMANDO INVALIDO, DIGITE NOVAMENTE')
    if seguir == 'N':
        break
    else:
        print('pfv... ', end=' ')
print(f'Foi digitado {tot} numeros ')


