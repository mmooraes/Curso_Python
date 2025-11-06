"""DESAFIO 034 - AULA 10

ESCREVE UM PROGRAMA QUE PERGUNTE O SALARIO DE UMA FUNCIONARIO E CALCULE O VALOR DO AUMENTO.

PARA SALARIO SUPERIORES A R$1.250,00, CALCULE UM AUMENTO DE 10%

PARA OS INFERIORES OU IGUAIS, O AUMENTO E DE 15%
"""

salario = float(input('Digite o salario para receber o aumento: ').replace(",", "."))
aumentoum = salario + (salario * 10 / 100)
aumentdois = salario + (salario * 15/ 100)

if salario > 1.250:
    print(f'Voce recebeu 10% de aumento: {aumentoum:.3f}')
else:
    print(f'Voce recebeu 15% de aumento: {aumentdois:.3f}')
