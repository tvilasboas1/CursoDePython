""" Crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com o nome "SANTO". """

cid = str(input('INFORME O NOME DA CIDADE:')).lstrip()

# O Upper vai converter tudo para maisculo fazendo a forma que digita o nome da cidade ser indiferente

print('NOME DA CIDADE: {}'.format(cid.upper()[0:5] == 'Santo')) # aqui o resultado sai como True e False


""" o [0:5] ou [:5] acima é para chamar o numero de caracteres da String em que é para apresentar e localizar, o == 'sANTO' que foi uma novidade"""