#TRANSFORMAÇÃO - AULA 09 C

frase = 'Curso em Video Python'

print(f'{frase.replace('Python', 'Android')}') # reaplace: realiza a troca de determinada palavra da string
print(f'{frase.upper()}') # upper: mantem o que é MAIUSCULO e coloca o restante em MAIUSCULO
print(f'{frase.lower()}') # lower: mantem o que é minisculo e coloca o restante em minusculo
print(f'{frase.capitalize()}') # capitalize: coloca somente a primeira letra em MAIUSCULO
print(f'{frase.title()}') # title: ele coloca a primeira letra de cada palavra em MAIUSCULO


frase2 = '   Aprendendo Python   '
print(f'{frase2.strip()}') # strip: Ela elimina os espaços antes e depois das frases
print(f'{frase2.rstrip()}') # rstrip: Ela elimina os espaços depois das frases
print(f'{frase2.lstrip()}') # lstrip: Ela elimina os espaços antes da frase