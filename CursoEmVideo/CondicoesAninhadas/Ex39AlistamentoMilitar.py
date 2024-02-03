"""Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:

Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo do alistamento.

Seu programa também deve mostrar quanto tempo falta ou quanto tempo passou do prazo."""

from datetime import date
anoatual = date.today().year
sexo = int (input("""Digite [1] para Sexo Masculino
Digite [2] para sexo Feminino. """))
nasc = int(input('Informe o ano de nascimento: '))
idade = anoatual- nasc

if sexo == 2: #colocado a opção de sexo apenas para embromar mesmo...
    print ('Alistamento não obrigatorio. ')

if idade < 18:
    id = 18 - idade
    anoAlist = (anoatual - idade) + 18
    print('Idade: {}\nJovem ainda ira se alistar em {}\nRestam {} anos'.format(idade, anoAlist, id))
elif idade ==18:
    print('Jovem no periodo de alistamento')
elif idade > 18:
    id = idade - 18
    anoAlist = (anoatual - idade) + 18
    print('Idade: {} \nJá passou do periodo de alistamento a {} anos.\nQue foi em {}'.format(idade, id,  anoAlist))
