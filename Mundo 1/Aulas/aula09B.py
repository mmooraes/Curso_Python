#ANÁLISE DE STRING

frase = 'Curso em Video Python'
print(f'{len(frase)}') #Len:  faz a contagem dos caracteries 
print(f'{frase.count('o')}') # cont: faz a contagem do que esta entre os ()
print(f'{frase.count('o', 0, 13)}') # cont: faz a contagem do que esta entre os () e tambem o fatiamento
print(f'{frase.find('deo')}') #find: ele mostra onde comerço o que esta em ()
print(f'{frase.find('android')}') #find: se ele n encontrar na string o que esta em () ele devolve -1
print(f'{'Curso'in frase}') #in frase: Mostra se a palavra entre 'xxx' existe na string