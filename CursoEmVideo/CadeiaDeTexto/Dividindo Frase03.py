#Split ao inves de apresentar 1 por 1 vai apresentar frase por frase.

frase = 'Curso em Video de Python 123'
print(frase.split()) #separador de espaço nas listas

dividido = frase.split()
print(dividido[0]) # a posição 0 também conta.
print(dividido[2]) # video nasce na posição 2 por exemplo
print(dividido [2] [3]) # aqui o 3 vai puxar o 'e' pois ele puxa a terceira casa da segunda posição.
