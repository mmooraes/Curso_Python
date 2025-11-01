"""DESAFIO 25 - AULA 09
CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DEFINA SE TEM
"SILVA" NO NOME
"""

cidade = str(input('Digite o seu nome completo: '))
print(f'{cidade}, tem "Silva" no nome?', "SILVA" in cidade.upper())