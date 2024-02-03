'''' Crie um programa que tenha uma Tupla com Varias Palavras ( não usar ascentos ). Depois disso, voce deve mostrar,
para cada palavra, quais são suas vogais. '''

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nA palavra {p.upper()} tem as vogais: ' ,end='') # pra destacar as Mauisculas

    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais, end='')
    print(f'\nA palavra {p.upper()} tem as conçoantes: ', end='')
    for concoantes in p:
        if concoantes.lower() in 'bcdfghjlmnpqrstvxyz':
            print(concoantes, end='')