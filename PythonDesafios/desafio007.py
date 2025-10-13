#Aula Tratando dados e fazendo contas: Desenvolva um programa que leia as duas notas de um aluno,
#calcule e mostre a media

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1+n2)/2
print(f'A média do aluno é: {m}') #o F pode ser usado para adicionar a variavel no texto.
if (m >= 5): 
    print('Parabéns, sua nota é {:.1f} Você foi aprovado!'.format(m))
else: 
    print('Que pena, sua nota foi {:.1f}. Você foi reprovado!'.format(m))