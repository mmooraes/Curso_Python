#FATIAMENTO DE STRING

frase = 'Curso em Video Python'
frase[9] #nesse caso ela busca o valor que esta na posição 9 da frase (nome da variavel + numero em [] ex: frase[9])
print(f'{frase[9]}')
frase[9:13] #Nesse caso ele conta do 9 ao 12, contando somente ate o numero anterior do informado
print(f'{frase[9:13]}')
frase[9:21] #nesse caso não é ideial utilzar numeros maior que a quantidade de caracteres, mas funciona
print(f'{frase[9:21]}')
frase[9:21:2] #Nesse caso vou comerçar no  9 e para no 21 (o :2 significa que ele vai saltar de 2 em 2)
print(f'{frase[9:21:2]}')
frase[:5] #Nesse caso que não há numero antes dos ' : ' ele inicia no 0 e vai te o numero informado depois do ' : '
print(f'{frase[:5]}') 
frase[15:] #Indica que vai ser lido do caracter 15 ate o final da frase
print(f'{frase[15:]}')
frase[9::3]  #Nesse caso começa no 9, e cada caracterie é mostrado de 3 em 3 casa - X . . X . . X . . X
print(f'{frase[9::3]}')