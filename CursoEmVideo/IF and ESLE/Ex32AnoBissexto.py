"""Faça um programa que leia um ano qualquer é mostre na tela se ele é Bissexto"""
""" Ano bissexto tem a regra dos 100 e 400 anos onde ele não é bissexto, alem de 4 em 4 anos. Ou seja o ano 1900 não é bissexto
o ano 1000 não é bissexto e por ai vai"""
from datetime import date

ano = int(input('Que ano quer analisar: ?? '))

if ano == 0:
    ano = date.today().year # Vai fazer o computador mostrar a data atual ^^

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print('O ano {} é Bissexo'.format(ano))
else:
    print('O ano de {} Não é Bissexto'.format(ano))

