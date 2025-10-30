"""DESAFIO 024 - AULA 09
CRIE UM PROGRAMA EM PY QUE LEIA O NOME DE UMA CIDADE E DIGA 
SE ELA COMEÇA OU NÃO COM O NOME SANTO
"""

cidade = str(input('Digite o nome da uma cidade: ')).strip()
if cidade.find('Santo') == 0:
    print(f'A cidade {cidade}, começa com Santo')
else:
    print(f'A cidade {cidade}, Não começa com Santo')