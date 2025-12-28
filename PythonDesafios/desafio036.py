'''Desafio 036 - Aula 12
Escreva um programa para aprovar o emprestimo bancario para compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestacao mensal, sabendo que a prestacao nao pode ultrapassar 30% do salario do comprador ou a pretencao sera negada.'''

casa = int(input('Qual o valor da casa que deseja comprar? R$'))
salario = int(input('Qual o seu salario? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

pagamento = (casa / anos)
if pagamento > (salario * 30 / 100):
    print(f'Infelizmente seu salario nao atende as normas')