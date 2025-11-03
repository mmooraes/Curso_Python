""" DESAFIO 029 - AULA 10
CRIE UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.

SE ELE ULTRAPASSAR 80Km/h, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO

A MULTA VAI CUSTAR R$ 7,00 PO KM ACIMA DO LIMITE
"""

import math

km = int(input('Digite a velocidade do veiculo: '))
multa = (km - 80) * 7

if km <= 80:
    print('Veiculo esta dentro da velocidade permitida')
else:
    print(f'Voce ultrapassou o limite de velocidade e foi multado em R${multa:.2f}')

