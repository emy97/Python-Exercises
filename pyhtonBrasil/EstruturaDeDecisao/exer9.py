#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))

lista = [num1, num2, num3]

lista.sort(reverse=True) #Coloca em ordem, e o reverse deixa em DESCRECENTE

print(f'{lista}')