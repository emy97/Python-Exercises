#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

for i in range(10):
    num = float(input(f'Digite o numero {i} : '))
    lista.append(num)

lista.reverse()
print(f'A lista é : {lista}')