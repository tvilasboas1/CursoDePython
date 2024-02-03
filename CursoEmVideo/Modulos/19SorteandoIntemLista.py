#professor quer sortear 4 alunos para apagar um quadro...

from random import choice

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
blablabla = [n1,n2,n3,n4] #blablabla foi só uma piada para lista
escolhido = choice(blablabla) #blablabla foi só uma piada para lista
print ('O aluno escolhido foi {}'.format(escolhido))

