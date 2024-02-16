'''

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
hr_valor = float(input('Digite o valor da hora : R$'))
total_hr_mes = int(input('Digite o total de horas no mês: '))

salario_bruto = hr_valor * total_hr_mes
print(f'+ Salário Bruto : R${salario_bruto:.2f}')

ir = salario_bruto * 0.11
print(f'- IR (11%) : R${ir:.2f}')

inss = salario_bruto * 0.08
print(f'- INSS (8%) : R${inss:.2f}')

sindicato = salario_bruto * 0.05
print(f'- Sindicato (5%) : R${sindicato:.2f}')

salario_liquido = (((salario_bruto - ir) - inss) - sindicato)
print(f'= Salário Liquido : R${salario_liquido:.2f}')

