""" DESAFIO 023 - AULA 09
FAÇA UM PROGRAMA DE LEIA O NUMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADOS

EX: 1834
UNIDADE: 4
DEZENA: 3
CENTENA: 8
MILHAR: 1
"""

numero = int(input('Digite um numero entre 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10 

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
