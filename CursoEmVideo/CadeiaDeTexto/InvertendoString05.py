#Da para organizar um Print de uma explicação longa

print(""" Agora vamos ver todos os metodos do Array 
 para que não fique confuso no futuro, deve checar depois
 no site do Phyton tudo para ver se tudo esta legal.""")

#essa budega imprime de qualquer jeito.

print('')

print('Curso em Video de Python 123')
frase = '   Curso Em Video de Python 123   ' #3 espaços antes e depois, pois é comum usuarios cometerem esses erros
print(frase)
print(len(frase))  #Naturalmente vai aparecer 34 espaços usados.
print(len(frase.strip())) #remove os espaços indesejaveis. Voltando para 28 espaços.

print(frase.replace('Python', 'Android')) #Troca a palavra Python pela palavra Android.
print(len(frase)) #ainda mantem as 34 caracteres com espaços da forma raiz.
# A String em seus micro elementos é imutavel, mas eu posso mudar e salva-la
frase = frase.replace('Python', 'Android')
print(frase) #Agora esta salvo na Memoria a alteração
print('Android' in frase ) #checando se a palavra esta na frase. é TAMBÉM mostra que ficou salvo.
print('Curso' in frase )
print('curso' in frase ) #Observação que mostra se esta com maiuscula e minuscula toda a informação.
print('frase' in frase)
print("""Checando agora a 
posição das Frases""")

print(frase.find('Video')) # Ponto de partida.
print(frase.find('Curso')) # entrou na posição 3 porque tem os espaços.
print(frase.find('curso'))# aqui mostra que não existe
print(frase.lower().find('curso')) #substitui o que esta em maisculo com minusculo
print(frase.find('Android'))