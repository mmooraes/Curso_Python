#Aula 15: faça um algoritimo que leia o preço de um produto
#e mostre seu novo preço, com 5% de desconto

precoReal = float(input('Qual o Valor do produro? R$ '))
Desconto = precoReal - (precoReal * 5 / 100)


print(f'O valor do produto é R${precoReal:.2f}, o valor final com 5% de desconto é R${Desconto:.2f}')