"""DESAFIO 033 - AULA 10
FACA UM PROGRAMA QUE LEIA TRES NUMEROS E MOSTRE QUAL E O MAIOR 
E QUAL E O MENOR 
"""
a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

menor = a
# verificando que e o menor
if b < a and b > c:
    menor = b
if c < a and c < b:
    menor = c
# maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print (f'O menor valor digitado foi: {menor}')
print (f'O maior valor digitado foi: {maior}')