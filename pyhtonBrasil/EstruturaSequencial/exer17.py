'''
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 
 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

print('Loja de tintas')
area = float(input('Digite a area em metros quadrados: '))
cobertura = area / 6
latas = int(cobertura / 18)
preco = 0.0
if cobertura % 18 != 0:
    latas += 1
    preco = latas * 80.0
    print(f'Latas usadas {latas}, preço total R${preco:.2f}')

galoes = int(cobertura /3.6)
if cobertura % 3.6 != 0:
    galoes += 1
    preco = galoes * 25.0
    print(f'galoes usados {galoes}, preço total R${preco:.2f}')

cob_folga = cobertura + (cobertura * 0.1)
resto = cob_folga % 18

print(f'cobertura folga {cob_folga}')

latas = int(cob_folga / 18)
galoes = int(resto /3.6)

if cob_folga > 18:
    if cob_folga % 18:
        if resto % 3.6 != 0:
            preco = latas * 80.0
            preco = preco + (galoes * 25.0)
            print(f'A fim de evitar desperdicio e uma folga de 10%, o correto seria: LATAS {latas} GALOES {galoes}, preço total R${preco:.2f} ')
elif cob_folga % 3.6 != 0:
    galoes += 1
    preco = galoes * 25.0
    print(f'A fim de evitar desperdicio e uma folga de 10%, o correto seria usar apenas,total de GALOES {galoes} , preço total R${preco:.2f}')
