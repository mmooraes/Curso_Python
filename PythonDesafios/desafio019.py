"""DESAFIO 019 - AULA 08
UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UMA PROGRAMA 
QUE LEIA O NOME DELES ESCREVENDO O NOME DOS ECOLHIDOS 
"""

import random
alunoUm = str(input('Aluno 01: '))
alunoDois = str(input('Aluno 02: '))
alunoTres = str(input('Aluno 03: '))
alunoQuatro = str(input('Aluno 04: '))
sorteado = random.randint(1,4)

print(f'Os aulunos são: \n 01- {alunoUm} \n 02- {alunoDois} \n 03- {alunoTres} \n 04- {alunoQuatro}')
print(f'O Aluno sorteado é {sorteado}')

    