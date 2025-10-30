"""DESAFIO 026 - AULA 09
FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
- QUANTAS VEZES APARECE A LETRA "A"
- EM QUE POSIÇÃO ELA APARECE PELA PRIMEIRA VEZ
- EM QUAL POSIÇÃO ELA APARECE PELA ULTIMA VEZ
"""

frase = str(input('Digite uma frase: ')).strip()

print('A letra "A" aparece',{frase.upper().count('A')})
print('A primeira letra "A" aparece na posição:', {frase.upper().find('a')})