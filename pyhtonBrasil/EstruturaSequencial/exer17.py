'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias
'''

tamanho = float(input("Digite o tamanho em metros quadrados: "))

litros = tamanho / 6
latas = int(litros / 18)
galoes = float(litros /3.6)

if latas % 18 != 0:
    latas += 1

print(f'Total de litros na obra: {litros:.2f}')
print(f'Total de latas necessarias : {latas}')

if galoes % 3.6 != 0:
    galoes += 1

print(f'Total de Galões necessarios: {galoes:.2f}')

tamanho_margem = tamanho +( tamanho * 0.1)
    





