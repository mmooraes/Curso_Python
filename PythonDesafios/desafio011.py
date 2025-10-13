#Aula Tratando dados e fazendo contas: Faça um programa que leia a largura e a altura de uma parade em metros
#calcule a sua área e a quantidade de tinta nescessaria para pintá-la
#sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
litros = area/2

print(f'Sua parede tem uma área de {area:.2f}m², considerando que cada lata pinta 2m², voce vai precisar de {litros:.1f}L de tinta para pintar a área')