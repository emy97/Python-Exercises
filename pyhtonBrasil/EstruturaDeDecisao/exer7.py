#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))

num_maior = max(num1, num2, num3)
num_menor = min(num1, num2, num3)

if num1 == num2 == num3:
    print('Ambos os numeros são iguais, sem maior ou menor')
else:
    print(f'O maior numero é {num_maior:.2f}')
    print(f'O menor num é {num_menor:.2f}')