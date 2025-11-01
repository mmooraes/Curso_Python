"""DESAFIO 16 - AULA 08 
Crie um programa que leia um numero Real qualquer 
pelo teclado e mostr na tela sua porção inteira
"""
from math import trunc

numero = float(input('Digite um numero real: '))
inteiro = trunc(numero)

print(f'A porção inteira de {numero} é {inteiro}')
print(f'A porção inteira de {numero} é {int(numero)}') #nesse caso n precisa de exportar e biblioteca