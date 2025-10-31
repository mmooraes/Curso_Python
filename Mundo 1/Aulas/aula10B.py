n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'Sua media é: {m:1.5}')
if m >= 6.0:
    print('Sua media foi boa')
else:
    print('Sua media foi ruim')