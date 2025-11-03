"""DESAFIO 030 - AULA 10
CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA
SE ELE E PAR OU IMPAR
"""

n = int(input('Digite um numero: '))

if n % 2 == 0:
    print(f'O numero {n} e PAR!')
else:
    print(f'O numero {n} e IMPAR!')