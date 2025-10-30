"""DESAFIO 027 - AULA 09
FAÇA UM PROGRAM EM PY QUE LEIA O NOME COMPLETO DE UMA PESSA,
MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE
"""
nome = str(input('Digite seu nome completo: ')).strip()
print(f'O nome completo é {nome}')
print('O primeiro nome é: ', nome.split()[0])
print('O ultimo nome é: ', nome.rsplit())