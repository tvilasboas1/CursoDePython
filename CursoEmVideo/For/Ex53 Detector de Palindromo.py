""" Crie um pograma que leia uma frase qualquer é diga se ela é um PALINDROMO, desconsiderando os espaços.
EX: Ler de trás para frente
"""

frase = str(input('Informe uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) # aqui vai juntar a frase.
inverso = ''
print('Voce digitou a Frase {}'.format(frase))
print(palavras) # Aqui mostra elas tendo espaços
print(junto) # Aqui imprime tudo junto
print(len(junto)) # vai contar quantas letras tem

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto [letra]

print(junto, inverso)
if junto == inverso:
    print('E Paldindromo')
else:
    print('Não é Palindromo')