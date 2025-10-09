#Crie um programa que leia quanto dinheiro uma pessoal
#tem na carteira e mostre quantos Dólares ela pode comprar
#considere US$ 1,00 = R$ 3,27

carteira = float(input('Digite o valor presente na carteira: '))
dolar = (float(3.27))
conversao = carteira/dolar

print(f'Voce tem na carteira R$ {carteira:.2f}. Voce pode comprar US$ {conversao:.2f}')
