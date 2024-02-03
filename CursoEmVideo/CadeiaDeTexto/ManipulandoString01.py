#Aula de Manipulação de Texto ou ArrayList

frase = ('Curso em Video Python 123')
print(frase)
print('')
print(frase[3])  # vai imprimir o terceiro caractere
print (frase[3:13])#vai imprimir do terceiro ao decimo segundo caractere... OBS: Sempre imprime o caractere antecessor, ou seja, marcou 13 ai imprime ate o 12.
print (frase[3:13:2])#vai imprimir de 2 em 2 espaços
print (frase [4:20:3])#mudando para testar imprimir de 4 em 4 espaços
print(frase[1::2])#foi retirado o final, apenas o inicio e o salto de 2 em 2
print(frase[::3])#foi retirado o inicio e o final, deixando apenas o salto de 3 em 3 letras
print(frase[:22:2])#Sem inicio, apenas com meio e final de 2 em 2 letras
print(frase[:5] == 'Curso') #Fara uma verificação para ver se localiza a palavra "curso" dentro da String
#So funciona com as primeiras letras pelo motivo obvio da String correr da Direita para a Esquerda







