#Altere o programa anterior para mostrar no final a soma dos números.
min = int(input('Digite um numero minino: '))
max = int(input('Digite um numero max:  '))
soma = 0
for i in range(min + 1, max):
    soma += i 
    print(f'{i}')

print(f'A soma dos números é: {soma}')