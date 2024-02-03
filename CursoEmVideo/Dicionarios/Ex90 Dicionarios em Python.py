'''Faça um programa que leia NOME E MEDIA de um aluno, guardando também a situação em um DICIONARIO. No final,
mostre o conteudo da estrutura na tela.
 Situação e para mostrar na tela se ele estara aprovado ou reprovado.
 '''


aluno = {}

aluno['Nome'] = str(input('Informe o nome do aluno -> '))
n1 = float(input('Informe a N1: '))
n2 = float(input('Informe a N2: '))
media = (n1 + n2) /2
aluno['Media'] = media
print('')

if media >= 60.0:
    aluno['Situação'] = 'APROVADO'
elif media > 50.0 and media < 60.0:
    aluno['Situaçao'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print(f'HISTORICO DO ALUNO: {aluno}')

for k, v in aluno.items():
    print(f' --> {k} --> {v}')