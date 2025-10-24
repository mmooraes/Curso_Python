"""DESAFIO 22 - AULA 09
CRIE UM PROGRAM QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:

- O NOME COM TODAS AS LETRAS MAIUSCULAS
- NO ME COM TODAS AS LETRAS MINUSCULAR
- QUANTAS LETARS AO TODO (SEM CONSIDERAR OS ESPÇOS)
- QUANTAS LETRAS TEM AO PRIMEIRO NOME
"""

nome = str(input('Digite seu nome completo: '))

print(f'{nome.upper()}')
print(f'{nome.lower()}')
print(f'O seu nome completo tem {len(nome.strip())} caracteres')
contagem = nome.split()
print(f'O primeiro nome tem {len(contagem[0])}')