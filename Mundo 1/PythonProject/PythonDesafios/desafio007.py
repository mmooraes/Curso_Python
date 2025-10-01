#Desenvolva um programa que leia as duas notas de um aluno,
#calcule e mostre a media

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1+n2)/2
print('A media do aluno e: {}'.format(m))
if (m >= 5): print('Parabens! Sua nota e {} Voce foi aprovado'.format(m))
else: (m <= 5); print('Que pena, sua nota foi {}. Voce foi reprovado'.format(m))