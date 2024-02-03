# \033[0;33;44m
#     0  -   nome
#    1 - bold ( negrito )
#    4 - underline
#    7 - negative

""" Text    back
        30 40  - branco
        31 41  - vermelho
        32 42 - verde
        33 43 - amarelo
        34 44 - azul escuro
        35 45 - roxo
        36 46 - azul claro
        37 47 - cinza
        """

"""\033[0;30;41m
\033[4;33;44m
\033 [1;35;43m
\033[30;42m #aqui nao colocou o padrao de estilo, no caso seria o Zero.
\033[m #cor padrao do terminal
\033[7;30m] #30 é letra branca. """
soma = 19 // 2
soma2= 19 % 2

print(soma, soma2)
print('\033[7;33;44m Ola, MUndo!\033')
