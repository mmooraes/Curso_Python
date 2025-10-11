#Faça um algoritimo que leia o salario de um funcionario e mostre
#seu novo salário, com 15% de aumento 

salarioAtual = float(input('Digite o salário atual: '))
aumento = (salarioAtual/100) * 15
novoSalario = salarioAtual + aumento

print(f'O Salario atual é R${salarioAtual}. Seu novo salario é de R${novoSalario}')