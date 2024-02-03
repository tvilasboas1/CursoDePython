"""" Crie um programa onde o usuario digite uma expressão qualquer que use parenteses. Seu Aplicativo devera analisar se a expressão
passada esta com os parenteses abertos e fechados na ordem correta """


expr = str('Digite um numero: ')
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida ! ')
else:
    print('Sua expressão esta errada')