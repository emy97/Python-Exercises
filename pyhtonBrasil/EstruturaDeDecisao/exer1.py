#Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite o segundo numero: '))

if num1 > num2:
    print(f'Numero 1[{num1:.2f}] é maior que o numero 2[{num2:.2f}] !')
elif num1 < num2:
    print(f'Numero 2 [{num2:.2f}] é maior que o numero 1[{num1:.2f}] !')
else:
    print('Os numeros são iguais !!')