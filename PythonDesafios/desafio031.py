"""DESAFIO 031 - AULA 10
DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM.

CALCULE O PRECO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATE 200KM
E R$0,45 PARA VIAGENS MAIS LONGAS
"""


km = float(input('Qual a distancia da viagem em KM? '))
kmmenor = km * 0.50
kmmaior = km * 0.45

if km <= 200 == kmmenor:
    print(f'O valor da viagem passagem e: R${kmmenor} ')
else:
    print(f'O valor da passagem e de R${kmmaior}')

"""# METODO COM IF SIMPLIFICADO

km = float(input('Qual a distancia da viagem em KM? '))
print(f'Voce esta preste a começar uma viagem de {km}Km.')
preco = km * 0.50 if km <= 200 else km * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')"""
