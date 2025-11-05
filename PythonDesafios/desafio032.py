"""DESAFIO 032 - AULA 10
FACA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE E BISSEXTO
"""
import calendar
ano = int(input('Informe o ano para saber se ele e bissexto: '))

if calendar.isleap(ano) == True:
    print(f'O ano {ano} e bissexto!')
else:
    print(f'O anor {ano} nao e bisseto!')
