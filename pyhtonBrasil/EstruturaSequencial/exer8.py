#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hr = input('Digitye o valor do seu salario por hora: ')
total_hr_mes = input('Quantas horas foram trabalhadas esse mês? ')

salario_hr_float = float(salario_hr)
total_hr_mes_float = float(total_hr_mes)

salario_mensal_recebido = total_hr_mes_float * salario_hr_float

print(f'O salario recebdio esse mês é de R${salario_mensal_recebido:.2f} ')

