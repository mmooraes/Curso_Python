"""DESAFIO 035 - AULA 10
DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRES RETAS E DIGA AO USUARIO
SE ELAS PODEM OU NAO FORMAR UM TRIANGULO
"""
cores = {'verde': '\033[0;32m',
        'limpa': '\033[m',
        'verdeeamarelo': '\033[1;32;43m',
        'vermelho': '\033[0;31m'}

print('-=' * 20)
print(' ' * 7, f'{cores['verdeeamarelo']} CALCULANDO UM TRIANGULO {cores['limpa']}')
print('-=' * 20)
a = float(input('Digite o valor A: '))
b = float(input('Digite o valor B: '))
c = float(input('Digite o valor C: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print(f'{cores['verde']}Parabens! Voce tem um triangulo{cores['limpa']}')
else:
    print(f'{cores['vermelho']}Que pena! Voce nao tem um triangulo{cores['limpa']}')