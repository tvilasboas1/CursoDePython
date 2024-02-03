# Todos operadores aritmeticos basicos testados
# já feitos no estilo .format
#
n1 = int (input('Informe um numero p/ A: '))
n2 = int (input('Informe um Numero p/ B: '))
s1 = n1 + n2
s2 = n1 - n2
s3 = n1 * n2
s4 = n1 / n2
s5 = n1**n2 #exponenciação
s6 = n1//n2 #divisao sem resto (exata)
s7 = n1 % n2 #resto
## Se quiser calulcar a raiz quadrada de um numero é só colocar ele na exponeciação elevado a 1\2
## 81**(1\2) sairia a raiz quadrada de 81. 81**(1/3) sairia a raiz cubica de 81

print ('Soma:{} Subtração:{} Multiplicação:{} Divisao:{} A elevado a B:{} DivisaoExata:{} Resto:{}'.format(s1,s2,s3,s4,s5,s6,s7))
## usar o end= faz puxar a linha de baixo e não pular
print ('Soma:{}\nSubtração:{}\nMultiplicação:{}\nDivisao:{}\nA elevado a B:{}\n DivisaoExata:{}\nResto:{}\n'.format(s1,s2,s3,s4,s5,s6,s7))
