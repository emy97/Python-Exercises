#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []
for i in range(5):
    num = int(input(f'Digite o numero {i}: '))
    lista.append(num)
print(lista)