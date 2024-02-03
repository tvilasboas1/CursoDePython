'''''''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.' \
' Seu programa devera ler um numero pelo teclado entre ( 0 e 20 ) e mostra-lo por extenso'''''''''
# usuario tem que digitar o numero pelo teclado
# Se Digitar um numero que não seja entre 0 ~ 20 aparecer a mensagem de tentar novamente
# Se eu digitaar o numero 13 por exemplo o programa tem que retornar = TREZE




cont = ( 'zero', 'um', 'dois', 'tres', 'quatro,', 'cinco', 'seis',  'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'desessete ', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num >= 0 and num <=20: # pode ser também -> if 0 <= num <= 20:
        break
    else:
        print('PFV Tente novamente -> ', end=' ') # deixando tudo na mesma linha para ficar mais bonito
print(f'Foi digitado o Numero: {cont[num]}')

