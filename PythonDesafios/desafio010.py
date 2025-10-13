#Aula Tratando dados e fazendo contas: Crie um programa que leia quanto dinheiro uma pessoal
#tem na carteira e mostre quantos Dólares ela pode comprar
#considere US$ 1,00 = R$ 3,27 (use o dolar do dia)

carteira = float(input('Digite o valor presente na carteira R$'))
dolar = carteira / 5.38
euro = carteira / 6.22
pesoArgentino = carteira / 0.0038


print(f'Voce tem na carteira R${carteira:.2f}. Voce pode comprar US${dolar:.2f}')
print(f'Voce tem na carteira R${carteira:.2f}. Voce pode comprar €{euro:.2f}')
print(f'Voce tem na carteira R${carteira:.2f}. Voce pode comprar ${pesoArgentino:.2f}')
