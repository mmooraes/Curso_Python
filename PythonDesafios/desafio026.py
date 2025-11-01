"""DESAFIO 026 - AULA 09
FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
- QUANTAS VEZES APARECE A LETRA "A"
- EM QUE POSIÇÃO ELA APARECE PELA PRIMEIRA VEZ
- EM QUAL POSIÇÃO ELA APARECE PELA ULTIMA VEZ
"""

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "A" aparece',frase.count('A'), 'vezes na frase.')
print('A primeira letra "A" apareceu na posição:', frase.find('A')+1)
print('A última letra "A" apareceu na posição: ',frase.rfind('A')+1)