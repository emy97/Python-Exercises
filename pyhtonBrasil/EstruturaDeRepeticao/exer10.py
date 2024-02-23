#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

min = int(input('Digite um numero minino: '))
max = int(input('Digite um numero max:  '))

for i in range(min + 1, max):
    print(f'{i}')