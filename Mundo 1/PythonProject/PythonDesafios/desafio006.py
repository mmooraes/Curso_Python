# Crie um algoritimo que leia o seu dobro, triplo e a raiz quadrada

n1 = float(input('Digite um numero: '))
d = n1*2
t = n1*3
rq = (n1**(1/2)) #vai ensinar na proxima aula (mas consegui resolver usando um float na variavel n1)
print('O dobro de {} \n Triplo {} \n Raiz Quadrada {:.3f}'.format(n1, t, rq))