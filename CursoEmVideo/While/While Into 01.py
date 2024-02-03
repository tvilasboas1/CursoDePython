# While = Enquanto
"""" ENQUANTO não (x)
            Passo
        pega"""

"""" 
ENQUANTO não ( maçã)
    se(tem chao )
        PASSO
    se ( Não tem chão)
        PULA
    se (Tem moedas)
        PEGA
    PEGA
        """
    print('--'*7,'Começando', '--' * 7)
    """ 
    for c in range (1, 10):
        print(c)
    print('Fim)
    """

c = 1 # copiando o For acima
while c < 10:  # C vai caminhar ate o 10
    print(c)
    c = c + 1
print('Fim')

n = 1
while n != 0: # qualquer numero diferente de 0 faz continuar
    n = int(input('Digite um Numero ?:   ')) # a oppção 0 vai parar o laço
print('Fim')

r = 'S'
while r == 'S': # Enquanto eu digitar S o programa vai continuar rodando no laço.
    r = str(input(' Deseja Continuar: [S / N ] ')).upper()
print('Fim')