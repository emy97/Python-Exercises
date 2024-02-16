'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

tamanho_metros = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))

cobertura = tamanho_metros / 3.0

latas = int(cobertura / 18)

if cobertura % 18 != 0:
    latas += 1

print(f'Voce deve comprar {latas} ')

valor_total = latas * 80.00
print(f'Voce deve pagar R${valor_total:.2f}')


