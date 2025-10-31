""" DESAFIO 028 - AULA 10
ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NUMERO INTEIRO
DE 0 E 5 E PEÇA PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NUMERO
PELO COMPUTADOR

O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU
"""

from random import choice
import emoji

print('-=-' *20)
print('  ' *10, 'JOGO DE ADVINHAÇÃO')
print('-=-' *20)
n1 = int(input('De 0 a 5. Qual número estou pensando?'))
print('---' *20)
n = [0, 1, 2, 3, 4, 5]
n2 = choice(n)
if n2 == n1:
    print(emoji.emojize(':green_circle: - Parabens! Voce acertou!'))
else:
    print(emoji.emojize(f':red_circle: Voce errou! o meu número era {n2}'))
