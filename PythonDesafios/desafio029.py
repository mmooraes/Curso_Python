""" DESAFIO 029 - AULA 10
CRIE UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.

SE ELE ULTRAPASSAR 80Km/h, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO

A MULTA VAI CUSTAR R$ 7,00 PO KM ACIMA DO LIMITE
"""

"""MINHA LOGICA
km = float(input('Digite a velocidade do veiculo: '))
multa = (km - 80) * 7

if km <= 80:
    print('Voce esta dentro do limite. Tenha um bom dia!')
else:
    print(f'Voce ultrapassou o limite de velocidade. Deverá pagar uma multada de R${multa:.2f}')"""


#LOGICA DO PROFESSOR - Utilizou a estrutura somente com IF (condição simples)
km = float(input('Digite a velocidade do veiculo: '))
if km > 80:
    print('MULTADO! Você excedu o limite permitido que é de 80Km/h')
    multa = (km - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')

