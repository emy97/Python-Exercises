#Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))

if num1 > num2 and num1 > num3:
    print(f'o numero {num1:.1f}, é maior que o {num2:.1f} e {num3:.1f}')
elif num2 > num1 and num2 > num3:
    print(f'o numero {num2:.1f}, é maior que o {num1:.1f} e {num3:.1f}')
elif num3 > num1 and num3 > num2:
    print(f'o numero {num3:.1f}, é maior que o {num1:.1f} e {num2:.1f}')
else:
    print('Os numeros são iguais')


#Uma pequena melhoria seria a função MAX :  maior_numero = max(num1, num2, num3)
