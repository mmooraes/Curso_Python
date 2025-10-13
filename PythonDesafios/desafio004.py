#Aula Tratando dados e fazendo contas:
# faca um programa que leia algo pelo teclado e mostre na tela o 
# seu tipo premitivo e todas as informacoes possivel sobre ele

n = input('Digite algo: ')
print('O tipo primitivo desse valor e: ',type(n))
print('O valor digitado e um numero? ',n.isnumeric())
print('O valor digitado e uma letra? ',n.isalpha())
print('O valor digitado e um numero e letra?',n.isalnum())
print('O valor digitado esta somente com letras maiusculas?',n.isupper())
print('O valor digitado esta somente com letras minusculas? ',n.islower())
print('O valor digitado e composto por espacos? ',n.isspace())

