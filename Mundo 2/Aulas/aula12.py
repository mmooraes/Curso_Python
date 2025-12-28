#A seguir temos uma estrutura de dados alinhadas, por estar em sequencia.

nome = str(input('Qual e o seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Nome muito popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print(f'Prazer em te conhecer, {nome}!') 