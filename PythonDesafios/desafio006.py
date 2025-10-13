#Aula Tratando dados e fazendo contas: Crie um algoritimo que leia o seu dobro, triplo e a raiz quadrada

n1 = int(input('Digite um numero: '))
d = n1 * 2
t = n1 * 3
rq = n1**(1/2) #vai ensinar na proxima aula (mas consegui resolver usando um float na variavel n1)
#print('O dobro de {} é {} \n O Triplo de {} é {} \n A Raiz Quadrada {:.2f}'.format(n1, d, n1, t, rq))

# usando apenas 1 varivel (com o objetivo apenas para esse programa, caso precise guardar os numero... precisa das variaveis)

#Opção01 - 
#print('O dobro de {} é {} \nO Triplo de {} é {} \nA raiz quadrada de {} é {}'.format(n1, (n1*2), n1, (n1*3), n1, (n1**(1/2))))

#Opção01
print('O dobro de {} é {} \nO Triplo de {} é {} \nA raiz quadrada de {} é {}'.format(n1, (n1*2), n1, (n1*3), n1, pow(n1,(1/2))))