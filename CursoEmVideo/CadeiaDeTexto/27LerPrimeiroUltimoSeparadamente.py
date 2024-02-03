"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro é o ultimo nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza """

nome = str(input('INFORME O NOME COMPLETO DA PESSOA: ')).strip()
n = nome.split()    #Split fatia a palavra toda, ou no caso ai o nome todoo ao inves de uma unica letra como nas demais Strings
print("PRIMEIRO NOME --->> {}".format(n[0])) # por causa do Split chama a palavra ou nome no caso na posição 0
print('ULTIMO NOME ----->> {}'.format (n[len(n) -1])) #Python deixa viajar na maionese. Aqui ele deixa vc colocar o nome com split para separar todos nomes, ai o Len para somar tudo ai ao substrair ele puxa o ultimo nome.


#desta forma abaixo só nao deu certo por causa do 'len' pois não da para combinar ele junto com Split, ai tem que criar um metodo separado
"""nome = str(input('INFORME O NOME COMPLETO DA PESSOA: ')).strip()
nome.split() #Split fatia a palavra toda, ou no caso ai o nome todoo ao inves de uma unica letra como nas demais Strings
print("PRIMEIRO NOME --->> {}".format(nome.split()[0]))
print('ULTIMO NOME ----->> {}'.format(len(nome.split()) -1 ) )"""