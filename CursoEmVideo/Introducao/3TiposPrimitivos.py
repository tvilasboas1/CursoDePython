#Faça um programa que leia algo no teclado, mostre seu tipo primitivo é tudo sobre ele
a = input ('Digite algo:')
print ('O tipo primitivo deste valor é: ', type(a))
print ('E um numero: ', a.isnumeric()) #lembrando que o A é um objeto
print ('E Espaços: ', a.isspace())
print ('E alphaNumerico', a.isalpha())
print ('Esta em maisculas:', a.islower())
print ('Esta em minusculas:', a.islower())
print ('Esta capitalizada', a.istitle())
print('')
print('')
print('')

print('O tipo primitivo é:{}{}tipo:{}Numero:{}TemEspaços:{}AlphaNumerico:{}TemMaisculas:{}TemMinusculas:'.format(a,type(a),a.isnumeric(),a.isspace(),a.isalpha(),a.islower(),a.islower()))
# Esse exercicio esta sem sentido, mas foi apenas para metodo de aprendizado, ele esta com falhas