"""DESAFIO 18 - AULA 08
FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUEALQUER E MOSTRE NA TELA O VALOR DE SENO, COSSENO E TANGENTE DESSE ANGULO
"""

#import math (nesse caso precisa utilizar o math.xxxx 30)
from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O angulo de {angulo} tem o TANGENTE de {tangente:.2f}')