"""DESAFIO 035 - AULA 10
DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRES RETAS E DIGA AO USUARIO
SE ELAS PODEM OU NAO FORMAR UM TRIANGULO
"""

print('-=' * 20)
print(' ' * 8, 'CALCULANDO UM TRIANGULO')
print('-=' * 20)
a = float(input('Digite o valor A: '))
b = float(input('Digite o valor B: '))
c = float(input('Digite o valor C: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print(f'Parabens! Voce tem um triangulo')
else:
    print(f'Que pena! Voce nao tem um triangulo')