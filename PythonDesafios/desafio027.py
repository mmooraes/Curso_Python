"""DESAFIO 027 - AULA 09
FAÇA UM PROGRAM EM PY QUE LEIA O NOME COMPLETO DE UMA PESSA,
MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE
"""
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f'O nome completo é {n}')
print('Seu primeiro nome é: ', (nome[0]))
print('O ultimo nome é: ', (nome[len(nome)-1]))