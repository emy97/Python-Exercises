#Faça um programa que leia 5 números e informe o maior número.
numeros = []
for i in range(5):
    numero = int(input(f'Digite o {i + 1}º numero: '))
    numeros.append(numero)

maior = max(numeros)
print(f'Maior numero é {maior}')