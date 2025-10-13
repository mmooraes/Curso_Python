#Aula 15: 07Faca um programa que leia um numero inteiro e 
#mostre na tela o seu sucessor e o seu antecessor.

n1 = int(input('Digite um numero: '))
s = n1 + 1
a = n1 - 1
print('O numero ditado e {}, o seu antecessor e {}, e o seu  e sucessor é {}.'.format(n1, a, s))

# usando apenas 1 varivel (com o objetivo apenas para esse programa, caso precise guardar os numero... precisa das variaveis)

print('O numero ditado e {}, o seu antecessor e {}, e o seu  e sucessor é {}.'.format(n1, (n1-1), (n1+1)))