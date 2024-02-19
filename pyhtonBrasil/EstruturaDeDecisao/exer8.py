#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Digite o preço do primeiro produto: R$'))
produto2 = float(input('Digite o preço do segundo produto: R$'))
produto3 = float(input('Digite o preço do terceiro produto: R$'))

mais_barato = min(produto1, produto2, produto3)

if produto1 == produto2 == produto3:
    print('Todos os produtos tem o mesmo preço !!')
else:
    print(f'Você deve comprar o produto que custa R$:{mais_barato:.2f}')