# ORDEM DE PROCEDENCIA
# 1- ()
# 2- **
# 3- *, /, //, %   (uma // e divisao inteiro ex: 10//2 = 5..... e /  e divisao real 10/2 = 5.5) ---- (% significa resto da divisao)
# 4- +. -

# responda o valor de 5+3*2=
#print(5 + (3*2))
# responda o valor de 3*5+4**2=
#print((3*5) + (4**2))
# responda o valor de 3*(5+4)**2=
#print(3*(5+4)**2)
# Qual a raiz quadada de 81 - 25=
#print(81**(1/2))
#print(25**(1/2))
# Qual a raiz cubica de 127=
#print(127**(1/3))
#----------------------------------------------------------------------------------------------------------------------
#n = srt(input('Qual e o seu nome?'))
#print('Muito prazer, {:20}!'.format(n)) # :20 = serve realizar o alinhamento do texto, basta usar <>^ para a direcao
#print('Muito prazer, {:>20}!'.format(n))
#print('Muito prazer, {:<20}!'.format(n))
#print('Muito prazer, {:^20}!'.format(n))
#print('Muito prazer, {:=^20}!'.format(n))
#----------------------------------------------------------------------------------------------------------------------
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma e {}, \n o produto e {}, \n e a divisao e {:.3f}'.format(s, m, d), end=' ')# :.3f - serve para limitar as casas decimais --- end=' ' - serve para juntar as linhas
print('Divisao interira {} e Potencia {}'.format(di, e))