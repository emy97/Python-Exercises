#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
acumulo = []
par = []
impar = []

for i in range(20):
    num = int(input(f'Digite o {i + 1} numero de 20: '))
    acumulo.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'Acumulo {acumulo}, par {par}, impar {impar}')
