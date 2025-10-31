""" DESAFIO 028 - AULA 10
ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NUMERO INTEIRO
DE 0 E 5 E PEÇA PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NUMERO
PELO COMPUTADOR

O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU
"""
import random
print ('JOGO DE ADVINHAÇÃO')

n1 = int(input('Qual numero voce acha que o computador pensou?: '))
n = [0, 1, 2, 3, 4, 5]
n2 = random.choice(n)
if n2 == n1:
    print('Parabens! Voce acertou')
else:
    print(f'Voce errou! o meu número era {n2}')