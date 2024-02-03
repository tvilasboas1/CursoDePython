#f = frase.split() # para fatear frases inteiras  ------ fzer depois

frase = ('curso em python -- CURSO EM PYTHON')

print (frase.capitalize()) #muda todos os caracteres para minusculo deixando apenas o primeiro caractere para Maiusculo
print(frase.title()) #Ele faz o contrario do (.capitalize ) pois ele pega todas palavras apos o paragrafo e coloca em caixa alta.

print('')

print(frase.strip()) #reduz os espaços colocado antes e depois da String, muitos usuarios erram
print(frase.lstrip()) #retira apenas os espaços da esquerda. O l = left
print(frase.rstrip())#retira apenas os espaços da direita. O R = Right

print('')

print(frase.split()) #divisão de palavras como mostra imprimido. Com esta divisão da para fazer muitas coisas
"""Obs: vc pode arrastar a String para frente e para tras usando operadores aritmeticos
por exemplo: (frase.split()) + 1 """

print('-'.join(frase)) #tenho que ver na pratica pois eu não entendi muito bem

