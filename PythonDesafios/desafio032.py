"""DESAFIO 032 - AULA 10
FACA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE E BISSEXTO
"""
"""
import calendar
ano = int(input('Informe o ano para saber se ele e bissexto: '))

if calendar.isleap(ano) == True:
    print(f'O ano {ano} e bissexto!')
else:
    print(f'O anor {ano} nao e bisseto!')"""


# MODO MATEMATICO
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO!')