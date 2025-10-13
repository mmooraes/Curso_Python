#Faça um algoritimo que leia o salario de um funcionario e mostre
#seu novo salário, com 15% de aumento 

salarioAtual = float(input('Digite o salário atual R$'))
aumento = salarioAtual + (salarioAtual * 15 / 100)
#aumento = (salarioAtual/100) * 15 # O metodo que utilizei usa mais linhas e mais tempo, o ideal é utilizar o mostratod pelo professor
#novoSalario = salarioAtual + aumento

print(f'O Salario atual é R${salarioAtual:.2f}. Seu novo salario é de R${aumento:.2f}')