"""DESAFIO 020 - AULA 08
O MESMO PROFESSOR DO DESAFIO ANTERIORO QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHO 
DOS ALUNO. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA
"""

from random import shuffle
a1 = str(input('Insisa o nome do aluno 01: '))
a2 = str(input('Insira o nome do aluno 02: '))
a3 = str(input('Insira o nome do aluno 03: '))
a4 = str(input('Insira o nome do aluno 04: '))
lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A ordem de apresentação é {lista}')
