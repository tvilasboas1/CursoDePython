""" sempre vai apresentar o numero de letras nas String e manipulalas.
pode somar ou subtrair elas também"""

frase = 'Curso Em Video de Python 123'
print(len(frase)) #Extremamente util, pois serve para checar o tamanho da frase
print(frase[5])#Vai imprimir a letra na casa 5
print(frase.count('o'))   #comando count para contar quantas vezes tem a letra solicitada.
print(frase.count('C')) #C maiusculo
print(frase.count('c'))  #Lembrando que diferencia Maiscula de Minusculas
print(frase.count('2')) #leitura de numero perfeitaa
print(frase.upper().count('e'))