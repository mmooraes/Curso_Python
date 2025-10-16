#Aula 8 – Utilizando Módulos 
#Itrodução

import math # o import serve para trazer um biblioteca (math = matematica)
num = int(input('Digite um número: '))
raiz = math.sqrt(num) #sqrt é o importe de operação para raiz

print(f'A raiz de {num} é igual a {raiz:.2f}')
print(f'A raiz de {num} é igual a {math.ceil(raiz)} com o arrendamento para cima') #ceil é o import de arredondamento para cima
print(f'A raiz de {num} é igual a {math.floor(raiz)} com o arredondamento para baixo') #floor é o import que faz o arrendondamento para baixo