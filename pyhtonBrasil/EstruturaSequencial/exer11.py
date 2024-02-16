'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.

'''

int1 = int(input('Digite um numero inteiro: '))
int2 = int(input('Digite o segundo numero inteiro: '))
num_real = float(input('Digite um numero real: '))

produto = (int1 * 2) * (int2 / 2)
soma = (int1 * 3) + num_real
cubo = num_real ** 3

print(f'PRODUTO: {produto}, SOMA: {soma:.2}, CUBO: {cubo:.3f}')
