#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
import numpy

num = []
soma = 0
mult = 0

for i in range(5):
    numeros = int(input(f'Digite o {i + 1} numero:  '))
    soma += numeros
    num.append(numeros)

mult = numpy.prod(num)

print(f'os numeros {num}, a soma {soma}, o produto deles {mult}')
