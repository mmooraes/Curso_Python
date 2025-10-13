'''
Crie um programa que leia o preço de um produto e calcule o valor de desconto de 10% para pagamento avista e com aumento de 8% para parcelado
'''

produto = float(input('Qual o Valor do produto? R$'))
avista = produto - (produto * 5 / 100)
aprazo = (produto * 8 /100) + produto

resposta = input('O pagamento do produto será avista? (Sim ou Não): ')

if resposta == 'Sim' or 'sim':
    print(f'O valor avista é de R${avista}')
else:
    print(f'O valor parcelado é de R${aprazo}')