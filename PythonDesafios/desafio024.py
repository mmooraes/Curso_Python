"""DESAFIO 024 - AULA 09
CRIE UM PROGRAMA EM PY QUE LEIA O NOME DE UMA CIDADE E DIGA 
SE ELA COMEÇA OU NÃO COM O NOME SANTO
"""

cidade = str(input('Digite o nome da uma cidade: '))
print(f'a cidade {cidade} tem ou não "Santo" no nome?', "Santo" in cidade)