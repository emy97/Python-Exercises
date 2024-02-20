'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
>salários até R$ 280,00 (incluindo) : aumento de 20%
>salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
>salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
>salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, 

informe na tela:
>o salário antes do reajuste;
>o percentual de aumento aplicado;
>o valor do aumento;
>o novo salário, após o aumento.
'''

print('----Programa de reajusta salarial ----')

salario_base = float(input('Digite seu salario atual: '))
reajuste = 0.0

if salario_base <= 280:
    reajuste = 0.2
elif salario_base <= 700:
    reajuste = 0.15
elif salario_base <= 1500:
    reajuste = 0.1
else:
    reajuste = 0.05


print(f'Salario antes do reajuste R${salario_base:.2f}')
print(f'O porcentual do aumento: {reajuste*100:.0f} %')
print(f'Valor aumentado R${salario_base * reajuste:.2f}')
print(f'Novo salario R${salario_base + salario_base * reajuste:.2f}')

