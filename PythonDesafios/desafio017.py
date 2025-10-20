""" DESAFIO 17 - AULA 8
Faça um programa que leia o comprimento do cateto oposto e do cateto 
adjacente de um tringulo retangulo, calcule e mostre o comprimento da hipotenusa
"""

"""
#AQUI USAMOS O METODO MATEMATICO 
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjascente: '))
hipotenusa = (oposto**2 + adjacente**2) ** (1/2)

print(f'A soma do cateto oposto {oposto} + o adjacente {adjacente} resulta no comprimento da hipotenusa de {hipotenusa:.2f}')
"""

#AQUI VAMOS UTILIZAR IMPORTAÇÃO DE BIBLIOTECA
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)

print(f'A soma do cateto oposto {co} + o adjacente {ca} resulta no comprimento da hipotenusa de {hi:.2f}')
