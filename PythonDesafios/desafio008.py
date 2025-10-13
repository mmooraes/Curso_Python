#Aula Tratando dados e fazendo contas: Escreva um programa que leia um valor em metros
#e o exiba convertido em centimetros e milimetros

n1 = float(input('Digite um valor em metros: '))
c = n1 * 100
mm = n1 * 1000
#print('O valor digitado: {:.2f}m! Sua conversão para centimetros: {:,.0f} cm, e em milimetros: {:_.0f} mm'.format(n1, c, mm).replace('_','.'))#
print('O Valor difitado: {:.2f}m! Sua conversão para centimentros: {:.0f}cm e em milimetros {:.0f}mm '.format(n1, c, mm))