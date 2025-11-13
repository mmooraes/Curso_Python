""" AULA 11 - teste de cores """ 

print('\033[1;31;31mOlá, Mundo!\033[m') #letra vermelhra
print('\033[4;30;45mOlá, Mundo!\033[m') #Letra branca e fundo lilaz
print('\033[7;37mOlá, Mundo!\033[m') # Fundo brando e letra preta
print('\033[0;33;44mOlá, Mundo!\033[m') #Fundo azul e letra branca

a = 3
b = 5

print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')

nome = 'Matheus'
print(f'Olá! Muito prazer em te conhecer, {'\033[4;34m'}{nome}{'\033[m'}!!!')

nomeum = 'Matheus'
cores = {'limpa': '\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco': '\033[7;30m'}
print(f'Olá! Muito prazer em te conhecer, {cores['amarelo']}{nome}{cores['limpa']}!!!')
print(f'Olá! Muito prazer em te conhecer, {cores['pretoebranco']}{nome}{cores['limpa']}!!!')