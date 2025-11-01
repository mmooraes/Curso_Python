"""DESAFIO 22 - AULA 09
CRIE UM PROGRAM QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:

- O NOME COM TODAS AS LETRAS MAIUSCULAS
- O NOME COM TODAS AS LETRAS MINUSCULAS
- QUANTAS LETRAS AO TODO (SEM CONSIDERAR OS ESPÇOS)
- QUANTAS LETRAS TEM O PRIMEIRO NOME
"""

nome = str(input('Digite seu nome completo: '))

print(f'{nome.upper()}')
print(f'{nome.lower()}')
print(f'O seu nome completo tem {len(nome) - nome.count(' ')} caracteres')
contagem = nome.split()
print(f'O primeiro nome tem {len(contagem[0])}')