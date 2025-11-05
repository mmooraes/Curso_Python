"""DESAFIO 031 - AULA 10
DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM.

CALCULE O PRECO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATE 200KM
E R$0,45 PARA VIAGENS MAIS LONGAS
"""

km = float(input('Qual a distancia da viagem em KM? '))
kmmenor = km * 0.45
kmmaior = km * 0.50

if km <= 200 == kmmenor:
    print(f'O valor da viagem passagem e: {kmmenor} ')
else:
    print(f'O valor da passagem e {kmmaior}')

