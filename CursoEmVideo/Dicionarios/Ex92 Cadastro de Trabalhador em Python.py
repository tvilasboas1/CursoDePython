'''Crie um programa que leia nome, ano de nascimento, carteira de trabalho e cadastre-os (com idade) se por acaso a CTPS for diferente de zero
o dicionario recebera também o ano de contratação e o salario. Calcule e apresente, alem de idade com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
dados = {}
dados['Nome'] = str(input('Informe o Nome ->> '))
nasc = int(input('Informe o Nascimeno ->> '))
dados['Nascimento'] = nasc
ctps = int(input('Informe o Numero da Carteira de Trabalho -> '))
if ctps != 0:
    dados['CTPS'] = ctps
    anocontratacao = int(input('Informe o Ano da 1° Contratação ->> '))
    aposentadoria = (anocontratacao + 35) - datetime.now().year
    dados['Ano de Contratação'] = anocontratacao
    dados['Salario'] = int(input('Informe o Salario -> '))
    dados['Aposentadoria'] = aposentadoria
else:
    dados['CTPS'] = ctps
    print('--' * 10)
    (print('Programa Encerrado. '))
print('--' * 10)
for k, v in dados.items():
    print(f'>>{k}: {v}')