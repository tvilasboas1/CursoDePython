#Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e antecessor.

n1 = int(input('informe um numero: '))
suc = n1+1
ant = n1-1

print('O numero informado:{}\nSeu Antecessor:{:7}\nSeu Sucessor:{:9} '.format(n1,ant,suc))

#devido ao meu Toc, coloquei tudo impresso e alinhado

#pode ser feito também... Colocando dentro do Format a soma para poupar memoria
# n1 = int(input('Informe um numero: '))
# print('O Numero Informado:{}Seu Antecessor:{}Seu Sucessor:{}'.format(n1,n-1),(n+1)))