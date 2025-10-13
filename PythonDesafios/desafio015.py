"""Aula 15:
Escreve um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelo quais foi alugado. Calcule o preço a pagar, sabendo que o carro custo 
R$60,00 por dia e R$0,15 por km rodado
"""

dias = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quantidade de KM percorrido: '))
apagar = (dias * 60) + (km * 0.15) 


print(f'O valor a ser cobrado será R${apagar:.2f} ')
