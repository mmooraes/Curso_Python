#DIVISÃO STRING - AULA 09

frase ='Curso em video Python'
print(f'{frase.split()}') # split: Ele divide string e palvras e faz uma lista 0- Curso 1- em 2- video 3- Python

#JUNÇÃO 

dividido = frase.split()
print(f'{'-'.join(dividido)}') # .join: ele coloca algum caracter entre as palvaras 
