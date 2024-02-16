'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

'''
sexo = int(input('Digite o numero referente ao seu sexo : HOMEM - 1 | MULHER - 2: '))
altura = float(input('Digite sua altura: '))

peso_hom = 0.0
peso_mul = 0.0

if sexo == 1:
    peso_hom = (72.7 * altura) - 58
    print(f'Seu peso ideal para HOMEM : {peso_hom:.2f}')
else:
    peso_mul = (62.1 * altura) - 44.7
    print(f'Seu peso ideal para MULHER: {peso_mul:.2f}')

