#Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []
for i in range(5):
    numero = int(input(f'Insira o {i} numero: '))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

print(f'A soma é {soma}')
print(f'A média é {media} ')