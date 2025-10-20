""" DESAFIO 17 - AULA 8
Faça um programa que leia o comprimento do cateto oposto e do cateto 
adjacente de um tringulo retangulo, calcule e mostre o comprimento da hipotenusa
"""

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjascente: '))
soma = (oposto**2 + adjacente**2)
hipotenusa = soma**(1/2)

print(f'A soma do cateto oposto {oposto} + o adjacente {adjacente} resulta no comprimento da hipotenusa de {hipotenusa}')

