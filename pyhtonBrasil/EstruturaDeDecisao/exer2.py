#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num1 = float(input('Digite um numero: '))

if num1 > 0:
    print(f'O numero digitado {num1:.2f} é POSITIVO .')
elif num1 < 0:
    print(f'O numero digitado {num1:.2f} é NEGATIVO .')
else:
    print(f'O numero digitado {num1:.2f} é NEUTRO .')