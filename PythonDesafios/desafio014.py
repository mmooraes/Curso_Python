"""Aula Tratando dados e fazendo contas:
Escreva um programa que converta uma temperatura digitada em °C e converta para °F
"""
c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
#nesse caso não precisamos utilizar o () por conta da ordem de precedecia 

print(f'A tempertura de {c}°C corresponde a {f}°F!')